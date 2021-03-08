from django.urls import path
from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products',
         ProductViewSet.as_view(
             {
                 'get': 'list',  # GET method will call list
                 'post': 'create'  # POST method wil call create function
             })),
    path('products/<str:pk>',
         ProductViewSet.as_view(
             {
                 'get': 'retrieve',  # GET method will call retrieve
                 'put': 'update',  # PUT method wil call update function
                 'delete': 'destroy'  # DELETE method wil call destroy function
             })),
    path('user',
         UserAPIView.as_view())
]
