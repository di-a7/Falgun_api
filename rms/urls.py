from django.urls import path, include
from .views import *
urlpatterns = [
   path('category', category),
   path('category/<id>/', category_detail)
]
