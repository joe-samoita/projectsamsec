from django.contrib import admin
from django.urls import path
from samsecapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('booking', views.index, name='booking'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', views.login, name='about'),
    path('home/', views.home, name='home'),
]
