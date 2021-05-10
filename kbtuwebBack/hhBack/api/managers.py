from django.db import models


class ProductsManager(models.Manager):
    def get_top_ten_products(self):
        return super(ProductsManager, self).get_queryset().order_by('-rating')[:10]
