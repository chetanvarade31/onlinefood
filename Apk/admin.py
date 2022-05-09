from django.contrib import admin

# Register your models here.
from .models import Customer, Hotels, Order, Product, Category, Reviews, Table


@admin.register(Category)

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Product)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','category']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','state','gender']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user','name','quantity','date','status']

@admin.register(Hotels)
class HotelModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Table)
class TableModelAdmin(admin.ModelAdmin):
    list_display = ['name','persons','date','time','hotel_name']

@admin.register(Reviews)

class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','user']