from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('play_game',views.guess_num,name='play_game')
]
