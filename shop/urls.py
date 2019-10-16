from django.urls import path
from . import views

urlpatterns = [
	path('', views.shop),
	path('api/shop/products', views.ProductsList.as_view())
]

