"""onlinefood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Apk import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name= 'home'),
    path('<slug:zpcode>',views.index, name= 'home'),
    path('breakfast/',views.breakfast, name= 'breakfast'),
    path('breakfast/<str:name>',views.breakfast, name= 'breakfast'),
    path('dinner/',views.dinner, name= 'dinner'),
    path('dinner/<str:name>',views.dinner, name= 'dinner'),
    path('lunch/',views.lunch, name= 'lunch'),
    path('lunch/<str:name>',views.lunch, name= 'lunch'),
    path('desserts/',views.dessert, name= 'dessert'),
    path('desserts/<str:name>',views.dessert, name= 'dessert'),
    path('productdetails/',views.productdetail, name= 'productdetails'),
    path('productdetails/<slug:data>',views.productdetail, name= 'productdetails'),
    # path('sami/',views.sami, name= 'sami'),
    path('payment/',views.payment, name= 'payment'),
    path('payment/<slug:data>',views.payment, name= 'payment'),
    path('order/',views.order, name= 'order'),
    path('order/<slug:id>/<int:qun>',views.order, name= 'order'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('profile/',views.profile,name='profile'),
    path('signout/',views.signout , name= 'signout'),
    path('offline/',views.offline , name= 'offline'),
    path('hotels/',views.hotels , name= 'hotels'),
    path('hotels/<str:name>',views.hotels , name= 'hotels'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
