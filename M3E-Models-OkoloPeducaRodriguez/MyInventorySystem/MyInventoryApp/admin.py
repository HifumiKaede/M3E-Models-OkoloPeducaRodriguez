from django.contrib import admin
from.models import Supplier, WaterBottle

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','city','country','created_at')

@admin.register(WaterBottle)
class WaterBottleAdmin(admin.ModelAdmin):
    list_display = ('SKU','brand','cost','size','mouth_size','color','supplied_by','current_quantity')

# Register your models here.
