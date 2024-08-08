from django.urls import path
from .views import run_code, index

urlpatterns = [
    path('', index, name='index'),
    path('run/', run_code, name='run_code'),
]
