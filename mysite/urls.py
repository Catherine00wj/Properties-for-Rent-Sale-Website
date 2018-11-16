"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from Search import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',include('register.urls')),
    path('captcha/',include('captcha.urls')),
    path('login/',include('login.urls')),
    path('InforRealease/',include('InforRealease.urls')),
    path('message/',include('message.urls')),
    path('Demandrelease/',include('Demandrelease.urls')),
    path('Search/',include('Search.urls')),
    path('Search_buy/',include('Search_buy.urls')),
    path('Demandmy/',include('Demandmy.urls')),
    path('comment/',include('comment.urls')),
    path('',views.home),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
