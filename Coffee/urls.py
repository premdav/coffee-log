from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.add_coffee, name='add-coffee'),
  path('edit/<int:coffee_id>', views.update_coffee),
  path('delete/<int:coffee_id>', views.delete_coffee),
]
