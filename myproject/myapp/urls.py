from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.moviedetail, name='movie_detail'),
    path('register/director/', views.registerdirector, name='registerdirector'),
    path('register/movie/', views.registermovie, name='registermovie'),
    path('writing/log/', views.writinglog, name='writinglog'),  
    path('update/log/<int:pk>/', views.updatelog, name='updatelog'),
    path('delete/log/<int:pk>/', views.deletelog, name='deletelog'), # この行を追加
    path('delete/movie/<int:pk>/', views.deletemovie, name='deletemovie'), # この行を追加
    path('writingthismovielog/movie/<int:pk>/', views.writingthismovielog, name='writingthismovielog'), 
]