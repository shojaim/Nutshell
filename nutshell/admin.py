from django.contrib import admin
from .models import Category, City, Inventory, InventoryProduct, Order, Product

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Inventory)
admin.site.register(InventoryProduct)
admin.site.register(Order)
admin.site.register(Product)

