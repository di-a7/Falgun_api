from rest_framework import serializers
from .models import Category
class CategorySerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField()
   
   def create(self, validated_data):
      category = Category.objects.create(name = validated_data.get("name"))
      return category


# validated_data = { "name": "Drink" }
# table: view, url, serializer