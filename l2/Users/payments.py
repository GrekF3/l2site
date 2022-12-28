from django.http import HttpResponse, HttpResponseRedirect
from requests import Response
from yookassa import Payment, Configuration, Refund
import uuid, json
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

Configuration.account_id = '969696'
Configuration.secret_key = 'test_o1nsEQBtHMeeb8zXKlrfH8OEsHtWgP0oI20ZcRwzeWI'

class YandexPayments(APIView):

    def get(self,request):
        payment = Payment.create({
                "amount": {
                    "value": "499.00",
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "http://127.0.0.1:443/order_completed/"
                },
                "capture": True,
                "description": "Оплата GOLD подписки на EzServers."
            }, uuid.uuid4())

        confrim_url = payment.confirmation.confirmation_url
        payment_id = payment.id
            
        return HttpResponseRedirect(confrim_url)
    

@csrf_exempt
def notifications(request):
    print(request.method)
    return HttpResponse(200)
    
