from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('guess/<str:player_name>/',views.guess,name='guess'),
    path('guess_num/<str:player_name>/',views.guess_num,name='guess_num'),
]
