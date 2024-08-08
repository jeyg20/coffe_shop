from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price", "creation_date_time"]
    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)
