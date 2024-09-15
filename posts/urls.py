from django.urls import path
from . import views




urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('create_post/', views.CreatePostView.as_view(), name="create_post"),
    path('edit_post/<slug:slug>', views.UpdatePostView.as_view(), name="edit_post"),
    path("detail/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("<slug:slug>/delete", views.DeletePostView.as_view(), name="delete_post"),
]