from django.urls import path
from .views import *

urlpatterns = [
    path('', releases),
    path('album/', album),
    
]
