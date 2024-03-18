from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import display_stories


urlpatterns = [

    path('story/<slug:slug>/', views.StoryDetailView.as_view(), name='stories_detail'),
    path('stories/', display_stories, name='display_stories'), 
    path('', views.StoryList.as_view(), name='home'),  
    path('story/', views.StoryList.as_view(), name='story'),
    path('profile/', views.profile_view, name='profile'),
    path('profile_picture_upload/', views.profile_picture_upload, name='profile_picture_upload'),
    path('set_avatar/', views.set_avatar, name='set_avatar'),
    path('accounts/', include('allauth.urls')),
    ##path('story/<slug:slug>/', StoryDetailView.as_view(), name='stories_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('submit-story/', views.submit_story, name='submit_story'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),
    
]
