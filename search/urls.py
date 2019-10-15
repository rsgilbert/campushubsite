from django.urls import path
from . import views

urlpatterns = [
	path('api/search/', views.SearchList.as_view()),
]