from django.urls import path
from .views import main, remove_todo

urlpatterns = [
    path('', main, name="main-page"),
    path('delete/<int:pk>', remove_todo, name="delete")
]
