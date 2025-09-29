# (LAB03)
from django.urls import path
from . import views

urlpatterns = [

]

# (LAB07)
urlpatterns = [
    path('', views.index, name='index'),
]