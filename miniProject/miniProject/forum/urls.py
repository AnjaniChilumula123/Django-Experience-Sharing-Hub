from django.urls import path

from forum import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-post/', views.userPost, name='user-post'),
    path('topic/<int:pk>/', views.postTopic, name='topic-detail'),
    path('search-result/', views.searchView, name='search-result'),
    path('blog-result/', views.blogView, name='blog-result'),
    path('user-dashboard/', views.userDashboard, name='user-dashboard'),
    path('upvote/', views.upvote, name='upvote'),
    path('downvote/', views.downvote, name='downvote'),
    path('blog/', views.blogListView, name='blog'),
    path('about/',views.about,name='about'),
    path('feedback/',views.feedback,name='feedback'),
    path('saveEnquiry/',views.saveEnquiry,name='saveEnquiry'),
    path('article/<slug:slug>/', views.blogDetailView, name='article-detail'),
]
