from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['id','name']

admin.site.register(Category, CategoryAdmin)

class MenuAdmin(admin.ModelAdmin):
   list_display = ['id', 'name','category','price']
   search_fields = ['name']
   list_filter = ['category']

admin.site.register(Menu, MenuAdmin)

class TableAdmin(admin.ModelAdmin):
   list_display = ['id', 'number', 'capacity','is_available']
   list_editable = ['is_available']
   
admin.site.register(Table, TableAdmin)

class OrderItemInline(admin.TabularInline):  # StackInline
   model = OrderItem

class OrderAdmin(admin.ModelAdmin):
   list_display = ['id', 'user','status','payment_status','total_price']
   list_filter = ['status', 'payment_status']
   search_fields = ['user__username']
   inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)