from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllObjects.as_view()),
    path('<int:pk>/delete/', views.deleteObject.as_view()),
    path('get/', views.Home.as_view()),
]
