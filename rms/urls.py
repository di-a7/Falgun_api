from django.urls import path, include
from .views import *
urlpatterns = [
   path('category', CategoryGenericView.as_view()),
   # path('category/<id>/', CategoryDetail.as_view())
]
