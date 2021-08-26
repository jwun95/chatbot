from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('chattrain', views.chattrain, name='chattrain'),
    path('chatanswer', views.chatanswer, name='chatanswer'),
]