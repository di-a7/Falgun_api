from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.
class UserAPIView(APIView):
   def post(self,request):
      username = request.data.get('username')
      password = request.data.get('password')
      if username == '' or password == '':
         return Response({'error': 'Username and password are required.'}, status=400)
      user = authenticate(username=username, password=password)   # User.objects.filter(username=username, password=password)
      if user:
         token,_ = Token.objects.get_or_create(user=user)
         return Response({"token":token.key,"username":username}, status=201)
      else:
         return Response({"detail":"Invalid user."})