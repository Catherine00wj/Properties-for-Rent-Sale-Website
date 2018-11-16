from django.urls import path

from . import views
app_name='Search_buy'
urlpatterns=[
    path('',views.search_buy,name='Search_buy'),
]