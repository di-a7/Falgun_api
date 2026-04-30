from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryModelViewset, basename='category')
router.register('menu', MenuModelViewset, basename='menu')
urlpatterns = [
   # path('category/', CategoryModelViewset.as_view({'get':'list','post':'create'})),
   # path('category/<pk>/', CategoryModelViewset.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
] + router.urls
