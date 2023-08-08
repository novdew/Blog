from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<int:pk>/', DetailPage.as_view(), name='detail'),
    path('<int:pk>/delete/', DeletePage.as_view(), name='delete'),
    path('<int:pk>/edit/', EditPage.as_view(), name='edit'),
    path('create/', CreatePage.as_view(), name='new'),
]
