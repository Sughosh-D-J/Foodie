from django.db import models
from shops.models import ShopDetails
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category,related_name='ProductCategory',on_delete=models.CASCADE)
    shops = models.ManyToManyField(ShopDetails)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Images(models.Model):
    images = models.ImageField(blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    shop = models.ForeignKey(ShopDetails,on_delete=models.CASCADE)
