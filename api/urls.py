
from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.HelloApi.as_view(), name = 'hello'),
    path('authhello/', views.AuthHelloApi.as_view(), name = 'authhello'),
    path('register/', views.Register.as_view(), name = 'register'),
    path('gettoken/', views.GetTokenApi.as_view(), name = 'get_token'),
]