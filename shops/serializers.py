from rest_framework import serializers
from .models import ShopDetails

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDetails
        fields = '__all__'
        order = ('-name_of_the_shop')

