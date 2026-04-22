from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=50)
   
   def __str__(self):
      return self.name

class Menu(models.Model):
   name = models.CharField(max_length=150)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   price = models.IntegerField()
   
   def __str__(self):
      return f"{self.name} - {self.price}"

class Table(models.Model):
   number = models.IntegerField(unique=True)
   capacity = models.IntegerField()
   is_available = models.BooleanField(default=True)
   
   def __str__(self):
      return f"Table {self.number} (Capacity: {self.capacity})"

class Order(models.Model):
   STATUS_CHOICES = [
      ("P", "Pending"),
      ("C", "Completed"),
      ("D", "Delivered"),
      ("X", "Cancelled"),
   ]
   PAYMENT_CHOICES = [
      ("P", "Pending"),
      ("C", "Completed"),
   ]
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="P", null=True, blank=True)
   payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default="P", null=True, blank=True)
   total_price = models.IntegerField(default=0, null=True, blank=True)

class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
   menu = models.ForeignKey(Menu, on_delete=models.PROTECT)