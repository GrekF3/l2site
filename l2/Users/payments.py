from yookassa import Payment, Configuration, Refund
import uuid

Configuration.account_id = '969696'
Configuration.secret_key = 'test_o1nsEQBtHMeeb8zXKlrfH8OEsHtWgP0oI20ZcRwzeWI'

payment = Payment.create({
    "amount": {
        "value": "499.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "http://127.0.0.1:8000/sucsess_order"
    },
    "capture": True,
    "description": "Оплата GOLD подписки на EzServers."
}, uuid.uuid4())

print(str(uuid.uuid4()))
print(payment.confirmation.confirmation_url)