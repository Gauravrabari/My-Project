"""
URL configuration for python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path

from GTA.views import *

from django.contrib.staticfiles.urls import * #staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('home/',home),
    path('master/',master),
    path('about/',about),
    path('services/',services),
    path('contact/',contact),
    path('ecommerce/',ecommerce),
    path('std_form/',std_form),
    path('Crud/',Crud),
    path('crud_input',crud_input),
    # path('registration/',registration),
    # path('login/', login),
    # path('profile/',profile),
    path('index/',index),
    
    path('delete_id/<int:id>/', delete_id),


    # path('01registration/', registration, name='registration'),
    # path('02login/', login_view, name='login'),
    # path('04profile/', profile, name='profile'),
    # path('02login/', login, name='login'),
    # path('03welcome/',welcome)




    #path('my-ip/', show_ip, name='show_ip'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()