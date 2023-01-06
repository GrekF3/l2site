import json
import uuid
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

class Payments(object):

    api_url = 'https://securepay.tinkoff.ru/v2'
    terminal_id = '1672740060359DEMO'
    password = 'ai2ui5rtwr721iwv'
    timeout = 1000
    
    def ini(self):
        self.TerminalKey = Payments.terminal_id
        self.password = Payments.password

    def Payment_Init(self):
        order_id = uuid.uuid4()
        id = str(order_id)

        data_json = {
            'TerminalKey':Payments.terminal_id,
            'OrderId':id,
            'Amount':49900,
            'Language':'ru',
            "Description": "Оплата покупки GOLD-подписки на сайте EzServers.",
        }

        init = 'Init'
        headers = {
            'Content-Type':'application/json'
        }
        response = requests.post(Payments.api_url + '/' + init, data=json.dumps(data_json), headers=headers)
        result = response.json()
        return result

def payment(request):
    payment = Payments()
    if request.user.is_authenticated:
        pay = payment.Payment_Init()
        URL = pay['PaymentURL']
        payment_id = pay['PaymentId']
        Order_id = pay['OrderId']
        return HttpResponseRedirect(URL)
    else:
        return redirect('auth')

@csrf_exempt
def checkpayment(request):
    if request.method == 'GET':
        response = request.GET
        data = json.dumps(response, ensure_ascii=False, indent=4)
        clear_data = json.loads(data)
        if clear_data['Success'] == 'true':
            user = request.user
            user.profile.Upgrade()
            messages.success(request,'Подписка успешно оплачена')
            return redirect('profile', user.profile.link)
        else:
            user = request.user
            error = clear_data['Message']
            message = f'Ошибка. {error}'
            messages.error(request, message=message)
            return redirect('profile', user.profile.link)



