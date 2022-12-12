from .models import Comments
from django.forms import ModelForm, Textarea, TextInput



class CommentsForm(ModelForm):

    class Meta:
        model = Comments
        fields = ("comment_text", 'commenter')

        widgets = {
            'comment_text':Textarea(attrs={
                'class':'form-control',
                'placeholder':'Ваш лучший комментарий!',
            }),
            'commenter':TextInput(attrs={
                'class':'form-control',
                'value':'111'
            }),
        }
