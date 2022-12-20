from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import BlogPost, Comments
from .forms import CommentsForm
from Users.models import UserIP
from django.contrib import messages



def get_client_ip(request):
    x_forwared_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwared_for:
        ip = x_forwared_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip

class BlogPostDetailView(FormMixin, DetailView):

    model = BlogPost
    template_name = 'blog-detail.html'
    context_object_name = 'post'
    form_class = CommentsForm

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_post = self.model.objects.get(slug=self.kwargs['slug'])
        comments = Comments.objects.all().filter(post=view_post).filter(moderate=True)

        context['comments_list'] = comments
        context['comments_form'] = self.get_form()


        # IP CHECKER
        ip = get_client_ip(self.request)
        if UserIP.objects.filter(ip=ip).exists():
            view_post.views.add(UserIP.objects.get(ip=ip))
            context['views'] = self.model.views
        else:
            UserIP.objects.create(ip=ip)
            view_post.views.add(UserIP.objects.get(ip=ip))
            context['views'] = self.model.views
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.warning(request,'Ваш комментарий отправлен на модерацию')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form.instance.post = self.model.objects.get(slug=self.kwargs['slug'])
        form.instance.commenter = self.request.user
        form.save()
        return super().form_valid(form)


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog.html"
    context_object_name = 'posts_list'

    def get_queryset(self):
        qs = self.model.objects.all().order_by("-date_published")
        return qs

    