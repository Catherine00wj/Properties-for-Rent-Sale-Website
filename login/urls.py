
from django.urls import path

from . import views
app_name='login'
urlpatterns=[
    path('',views.login,name="login"),
    path('login',views.login,name="login"),
    path('logoff',views.logoff,name="logoff"),
]