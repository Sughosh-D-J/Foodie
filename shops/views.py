from django.shortcuts import render
from rest_framework.response import Response
from .models import ShopDetails
from .serializers import ShopSerializer
from rest_framework.filters import SearchFilter
from rest_framework import generics

def home(request):
    return render(request,'home.html')


class Search(generics.ListAPIView):
    queryset = ShopDetails.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name_of_the_shop','land_mark']


