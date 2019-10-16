from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView

# Create your views here.
list_size = 30

def shop(request):
	return render(request, 'shop/shop.html')


class ProductsList(APIView):
	def get(self, request):
		products = Product.objects.all()[:list_size]
		data = ProductSerializer(products, many=True).data
		return Response(data)
	
