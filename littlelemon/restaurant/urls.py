# urls.py
#define URL route for index() view
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),    # The index() view renders the 'index.html' template when the root URL is accessed.
    path('menu/', views.MenuItemView.as_view(), name='menu_list_create'),  # Handles GET and POST requests for the menu list
    path('menu/<int:id>/', views.SingleMenuItemView.as_view(), name='menu_detail'),  # Handles GET, PUT, and DELETE for a single menu item
]

