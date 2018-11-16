
from django.urls import path

from . import views
app_name='register'
urlpatterns=[
    path('',views.register,name='register'),
    path('index',views.index,name="index"),
    path('userinfoin',views.userinfoin,name="userinfoin"),
    path('confirm',views.confirm,name="confrim"),
]