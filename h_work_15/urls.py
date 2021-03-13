from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('uslugi', views.uslugi, name='uslugi'),
    path('about', views.about, name='about'),
    path('news', views.ShowNewsView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/add', views.CreateNewsView.as_view(), name='news-add'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
    path('user/<str:username>', views.UserAllNewsView.as_view(), name='user-news'),
    path('comment', views.CreateComment.as_view(), name='comment'),
    path('comment/view', views.ShowComment.as_view(), name='comment-view'),
    ]
