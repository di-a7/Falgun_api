from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.serializers import ValidationError
from rest_framework import status
# from rest_framework.pagination import PageNumberPagination
from .paginations import MenuPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MenuFilter
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAuthenticatedorReadOnly
# Create your views here.
# ModelViewset
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

class CategoryModelViewset(ModelViewSet):
   queryset = Category.objects.all()     
   serializer_class = CategorySerializer
   permission_classes = [IsAuthenticatedorReadOnly]
   
   @extend_schema(
      parameters=[OpenApiParameter(name='name', description='Name of the category', type=OpenApiTypes.STR)],
      description='this handles category list',
   )
   def list(self, request, *args, **kwargs):
      return super().list(request, *args, **kwargs)
   
   def destroy(self, request, *args, **kwargs):
      category = self.get_object()#break
      item = OrderItem.objects.filter(menu__category = category).count()
      if item > 0:
         raise ValidationError({"details":"Data can not be deleted. Category relate to OrderItem"})
      category.delete()
      return Response({"detail":"Data has been deleted."})


class MenuModelViewset(ModelViewSet):
   queryset = Menu.objects.select_related('category').all()     
   serializer_class = MenuSerializer
   pagination_class = MenuPagination
   filter_backends = [filters.SearchFilter, DjangoFilterBackend]
   search_fields = ['name']      # Menu.objects.filter()
   # filterset_fields = ['category']
   filterset_class = MenuFilter
   permission_classes = [IsAuthenticatedorReadOnly]


class OrderModelViewset(ModelViewSet):
   queryset = Order.objects.all()     
   serializer_class = OrderSerializer
   permission_classes = [IsAuthenticatedorReadOnly]
   pagination_class = MenuPagination
   filter_backends = [filters.SearchFilter, DjangoFilterBackend]
   search_fields = ['user__username']
   filterset_fields = ['status','payment_status']


# Viewset
# from rest_framework import viewsets

# class CategoryViewset(viewsets.ViewSet):
#    def list(self, request):
#       category = Category.objects.all()     
#       serializer = CategorySerializer(category, many=True)           
#       return Response(serializer.data, status=status.HTTP_200_OK)
   
#    def create(self,request):
#       serializer = CategorySerializer(data = request.data)      
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CategoryDetailViewset(viewsets.ViewSet):
#    def retrieve(self,request, pk):
#       category = Category.objects.get(pk = pk)
#       serializer = CategorySerializer(category)           
#       return Response(serializer.data)





# Class Base view
# Mixins and generic API
# from rest_framework import mixins
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class CategoryGenericView(ListCreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer


# class CategoryDetailView(RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def delete(self, request, *args, **kwargs):
#       item = OrderItem.objects.filter(menu__category = self.get_object()).count()
#       if item > 0:
#          raise ValidationError({"details":"Data can not be deleted. Category relate to OrderItem"})
#       return self.destroy(request, *args, **kwargs)
      # return Response({"detail":"Data has been deleted."})



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