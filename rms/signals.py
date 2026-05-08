from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail
import requests
import mailtrap as mt


@receiver(post_save, sender = Order)
def save_order(sender, instance, created, **kwargs):
   print("Order has been created.")
   client = mt.MailtrapClient(
      token= "cc91362633696353b46c6d230fd5e300",
      sandbox=True,
      inbox_id=4426905
   )

   mail = mt.Mail(
      sender=mt.Address(email="test@example.com", name="Test Sender"),
      to=[mt.Address(email="user@example.com", name="Test User")],
      subject="Order Created",
      text="Your order has been created.",
      html="<p>Your order has been <b>created</b>.</p>"
   )
   client.send(mail)
   # url = f"https://sandbox.api.mailtrap.io/api/send/{inbox_id}"
   # requests.post(url, data = data, headers = {"Api-Token": api_key})






