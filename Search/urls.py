from django.urls import path

from . import views
app_name='Search'
urlpatterns=[
    path('',views.search_result,name='Search'),
    # path('rent',views.index,name="rent"),
    # path('buy',views.userinfoin,name="buy"),
    path('home/', views.home, name = 'home'),

]