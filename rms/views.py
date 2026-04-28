from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import CategorySerializer
from rest_framework.serializers import ValidationError
from rest_framework import status
# Create your views here.
# Class Base view
# Mixins and generic API
from rest_framework import mixins
from rest_framework import generics

class CategoryGenericView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
   def get(self, request):
      return self.list(self,request)
   
   def post(self,request):
      return self.create(self,request)

# create a class that handles retrieve, update, destroy using generic and mixin


# APIView
# from rest_framework.views import APIView

# class CategoryView(APIView):
#    def get(self, request):
#       category = Category.objects.all()     
#       serializer = CategorySerializer(category, many=True)           
#       return Response(serializer.data, status=status.HTTP_200_OK)
   
#    def post(self,request):
#       serializer = CategorySerializer(data = request.data)      
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CategoryDetail(APIView):
#    def get(self,request, id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category)           
#       return Response(serializer.data)






# function based view
# from rest_framework.decorators import api_view

# @api_view(['GET','POST'])
# def category(request):
#    if request.method == "GET":
#       category = Category.objects.all()      # [{'id': '1', 'name':"hello"}]
#       serializer = CategorySerializer(category, many=True)           # serialize: instance/queryset is converted into json format
#       return Response(serializer.data)
#    elif request.method == 'POST':
#       serializer = CategorySerializer(data = request.data)      # deserialize: json converted to class instance
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)

# @api_view(['GET','DELETE'])
# def category_detail(request, id):
#    category = Category.objects.get(id = id)      # [{'id': '1', 'name':"hello"}]
#    if request.method == 'GET':
#       serializer = CategorySerializer(category)           # serialize: instance/queryset is converted into json format
#       return Response(serializer.data)
   
#    elif request.method == 'DELETE':
#       item = OrderItem.objects.filter(menu__category = category).count()
#       if item > 0:
#          raise ValidationError({"details":"Data can not be deleted. Category relate to OrderItem"})
#       category.delete()
#       return Response({"detail":"Data has been deleted."})