from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('', views.add_resource, name='ResourceInfor'),
    path('detail/', views.view_detail, name = 'HouseDetail'),
    path('all/', views.view_all_resources, name = 'ResourceDisplay'),
    path('delete/', views.delete_resource, name = 'DeleteResource'),
    path('my/', views.view_my_resource, name = 'MyResource'),
    # path('home/', views.yimi, name = 'home'),
]
