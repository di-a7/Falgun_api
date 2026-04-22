from django.db import models

# Create your models here.
class Category(models.Model):# , Food
   name = models.CharField(max_length=50)
   
   def __str__(self):
      return self.name

class Menu(models.Model):
   name = models.CharField(max_length=150) # Coke, Sprite, Fanta
   category = models.ForeignKey(Category, on_delete=models.CASCADE)# NULL
   price = models.IntegerField()
   
   def __str__(self):
      return f"{self.name} - {self.price}"