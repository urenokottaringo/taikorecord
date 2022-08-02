from django.urls import path
from . import views

app_name = 'taikorecord'
urlpatterns = [
    path('',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),
    path('createAccount',views.AccountRegistration.as_view(), name='createAccount'),
    path('home', views.home, name='home'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('musicdetail/<int:pk>/', views.musicdetail, name='music_detail'),
    path('register/genre/', views.registergenre, name='registergenre'),
    path('register/music/', views.registermusic, name='registermusic'),
    path('writing/log/', views.writinglog, name='writinglog'),  
    path('update/log/<int:pk>/', views.updatelog, name='updatelog'),
    path('delete/log/<int:pk>/', views.deletelog, name='deletelog'), 
    path('delete/music/<int:pk>/', views.deletemusic, name='deletemusic'), 
    path('writingthismusiclog/music/<int:pk>/', views.writingthismusiclog, name='writingthismusiclog'), 
]