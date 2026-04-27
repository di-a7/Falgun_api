from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
# Create your views here.

@api_view()
def category(request):
   category = Category.objects.all()      # [{'id': '1', 'name':"hello"}]
   serializer = CategorySerializer(category, many=True)                 # instance/queryset is converted into json format
   return Response(serializer.data)

