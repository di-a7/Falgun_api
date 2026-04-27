from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import CategorySerializer
from rest_framework.serializers import ValidationError
# Create your views here.

@api_view(['GET','POST'])
def category(request):
   if request.method == "GET":
      category = Category.objects.all()      # [{'id': '1', 'name':"hello"}]
      serializer = CategorySerializer(category, many=True)           # serialize: instance/queryset is converted into json format
      return Response(serializer.data)
   elif request.method == 'POST':
      serializer = CategorySerializer(data = request.data)      # deserialize: json converted to class instance
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

@api_view(['GET','DELETE'])
def category_detail(request, id):
   category = Category.objects.get(id = id)      # [{'id': '1', 'name':"hello"}]
   if request.method == 'GET':
      serializer = CategorySerializer(category)           # serialize: instance/queryset is converted into json format
      return Response(serializer.data)
   
   elif request.method == 'DELETE':
      item = OrderItem.objects.filter(menu__category = category).count()
      if item > 0:
         raise ValidationError({"details":"Data can not be deleted. Category relate to OrderItem"})
      category.delete()
      return Response({"detail":"Data has been deleted."})