from django.urls import path
from .views import (
    CategoryView,
    HomeView,
    about,
    contact,
    profile,
    NewVideo,
    VideoView,
    CommentView,
    VideoFileView,
    CreateChannelView,
    ChannelView
)
from core import views
from accounts.views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('profile/<str:pk>', profile, name='profile'),
    path('video_category/<str:slug>', CategoryView, name='Video'),
    path('new_video', NewVideo.as_view()),
    path('video/<int:id>/<int:new>/', VideoView.as_view()),
    path('comment', CommentView.as_view()),
    path('get_video/<file_name>', VideoFileView.as_view()),
    path('createchannel', CreateChannelView.as_view()),
    path('<user>/channel', ChannelView.as_view()),
    path('video/<int:v_id>/<int:u_id>/like',
         views.video_like, name='video_like'),
    path('video/<int:v_id>/<int:u_id>/unlike',
         views.video_unlike, name='video_unlike'),
    path('video/<int:v_id>/<int:u_id>/dislike',
         views.video_dislike, name='video_dislike'),
    path('video/<int:v_id>/<int:u_id>/undislike',
         views.video_undislike, name='video_undislike'),
    path('liked/', views.liked_videos, name='liked_videos'),
    path('watch_history/', views.watch_history, name='watch_history'),
    path('trending/', views.trending, name='trending'),
    path('help/', views.help, name='help'),
    path('channel_subscribe/<int:c_id>/',
         views.channel_subscribe, name='channel_subscribe'),
    path('channel_unsubscribe/<int:c_id>/',
         views.channel_unsubscribe, name='channel_unsubscribe'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('channels_list/', views.channels_list, name='channels_list'),
    # path('signup', signup, name='signup'),
    # path('signin', signin, name='signin'),
    # path('logout', logout, name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
]
