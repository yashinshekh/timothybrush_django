from django.urls import path
from .views import *

urlpatterns = [
    path('shop/',view=shop,name='shop')
]
