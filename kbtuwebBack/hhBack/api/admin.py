from django.contrib import admin
from .models import Category, Product, Comment, MyUser

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product


admin.site.register(Comment)
admin.site.register(MyUser)


