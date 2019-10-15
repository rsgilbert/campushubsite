from django.shortcuts import render
from .models import SearchHistory
from shop.models import Product
from shop.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.



class SearchList(APIView):
	def get(self, request):
		searchword = request.GET.get('searchword')
		search_history = SearchHistory()
		search_history.seachword = searchword
		search_history.save()
		if searchword is not None:
			products = Product.objects.filter(name__icontains=searchword)
		else:
			products = Product.objects.all()
		data = ProductSerializer(products, many=True).data
		return Response(data)
	
