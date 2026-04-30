from django.urls import path, include
from .views import *
urlpatterns = [
   path('category/', CategoryModelViewset.as_view({'get':'list','post':'create'})),
   path('category/<pk>/', CategoryModelViewset.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
]
