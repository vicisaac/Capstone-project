#define URL route for index() view
from django.urls import path
from . import views
#from .views import UserListView, UserDetailView

urlpatterns = [
    path('', views.index, name='index'),

    # URL for listing all users
    #path('users/', UserListView.as_view(), name='user-list'),
    
    # URL for retrieving a specific user by username
    #path('users/<str:username>/', UserDetailView.as_view(), name='user-detail'),
]

# The index() view renders the 'index.html' template when the root URL is accessed.