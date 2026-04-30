from rest_framework import serializers
from .models import Category, Menu

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      # fields = '__all__'
      fields = ['id','name']
      # exclude = ['id']
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      data = validated_data.get('name')
      items = Category.objects.filter(name = data).count()
      if items > 0:
         raise serializers.ValidationError({"details":"Data already exist."})
      return super().save(**kwargs)


class MenuSerializer(serializers.ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   category = serializers.StringRelatedField()
   category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
   class Meta:
      model = Menu
      fields = ['id','name','category_id','category','price','price_with_tax']
   
   def get_price_with_tax(self, food:Menu):
      return 0.11 * food.price + food.price


# create a method that display price with 10% discount

# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()

#    def create(self, validated_data):
#       category = Category.objects.create(name = validated_data.get("name"))
#       return category


# validated_data = { "name": "Drink" }
# table: view, url, serializer