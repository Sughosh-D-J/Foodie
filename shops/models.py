from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

class ShopDetails(models.Model):
    slug = models.SlugField()
    name_of_the_shop = models.CharField(max_length=100)
    name_of_the_owner = models.CharField(max_length=100)
    phone = models.IntegerField()
    description = models.CharField(max_length=100)
    local_area_address = models.CharField(max_length=100,blank=False)
    land_mark = models.CharField(max_length=100)
    city = models.CharField(max_length=100,blank=False)
    state = models.CharField(max_length=100)
    pin_code = models.IntegerField()
    ratings = models.DecimalField(decimal_places=1,max_digits=3)
    shop_image = models.ImageField(upload_to='uploads',blank=True,null=True)

    class Meta:
        ordering = ('-name_of_the_shop',)

    def __str__(self) -> str:
        return self.name_of_the_shop
    
    def get_absolute_url(self):
        return f'/{self.ShopCategory.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000'+self.image.url
        return ''
    

class ShopCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    shops = models.ManyToManyField(ShopDetails)



