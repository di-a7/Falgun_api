from django.urls import path, include
from .views import category
urlpatterns = [
   path('category', category)
]
