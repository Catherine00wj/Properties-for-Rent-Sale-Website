from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_message, name='post_message'),
    path('inbox/', views.show_message, name='show_message'),
    path('inbox/delete/', views.del_message, name='del_message'),
    path('inbox/reply/', views.reply_message, name='reply_message'),
]