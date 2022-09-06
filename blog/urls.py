from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
     path('post_list', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('make_post', views.MakePostView.as_view(), name='make_post'),
    path('make_post', views.MakePostView.as_view(), name='make_post'),
]
