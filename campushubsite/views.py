from django.shortcuts import render


def handler404(request, exception):
	return render(request, 'shop/shop.html')

