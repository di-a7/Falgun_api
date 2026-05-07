from rest_framework import serializers
from .models import *

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


class OrderItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = OrderItem
      fields = ['menu']


class OrderSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default=serializers.CurrentUserDefault())
   status = serializers.CharField(read_only=True)
   payment_status = serializers.CharField(read_only=True)
   total_price = serializers.IntegerField(read_only=True)
   items = OrderItemSerializer(many=True)
   class Meta:
      model = Order
      fields = ['id','user','date','status','payment_status','total_price','items']
   
   def create(self, validated_data):
      items = validated_data.pop("items")
      self.total_price = 0
      for i in items:
         menu = i.get("menu")
         food = Menu.objects.get(id = menu.id)
         self.total_price += food.price
      order = Order.objects.create(**validated_data, total_price = self.total_price)
      # for i in items:
      #    menu = i.get("menu")
      #    OrderItem.objects.create(order = order, menu = menu)   
      # 3 quries
      # insert 1
      # insert 2
      # insest 3
      
      orderitems = [
         OrderItem(order = order, menu = i.get('menu')) for i in items
      ]
      orderitems = [OrderItem(order = 3, menu = 1),OrderItem(order = 3, menu = 3040),OrderItem(order = 3, menu = 3041)]
      OrderItem.objects.bulk_create(orderitems)    # insert value 1,2,3,4     1 query
      
      return order
      # return super().create(validated_data)

# validated_data={
#    "user":1}

# items = [
#     {
#       "menu": 1
#     },
#     {
#       "menu": 2
#     }
#   ]}



# create a method that display price with 10% discount

# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()

#    def create(self, validated_data):
#       category = Category.objects.create(name = validated_data.get("name"))
#       return category


# validated_data = { "name": "Drink" }
# table: view, url, serializer