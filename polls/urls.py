from django.urls import path
from . import views

urlpatterns = [
    path('hello/<int:id>', views.myfunc)
]