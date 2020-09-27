"""Busmanagment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bus.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',nav,name="nav"),
    path('about/',About,name="about"),
    path('login/',Login_customer,name="login_customer"),
    path('register_customer/',Register_customer,name="register_customer"),
    path('contact/',Contact,name="contact"),
    path('search_bus/',Search_Bus,name="search_bus"),
    path('dashboard/',Dashboard,name="dashboard"),
    path('dashboard2/',admindashboard,name="admindashboard"),
    path('addbus/',Add_bus,name="add_bus"),
    path('addroute/',add_route,name="add_route"),
    path('editbus/?P<pid>[0-9]+)',edit,name="editbus"),
    path('delete/?P<pid>[0-9]+)',delete,name="delete"),
    path('viewbus/',view_bus,name="view_bus"),
    path('availableroute/',displayroute,name="availableroute"),
    path('log_out/',Logout,name="log_out"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
