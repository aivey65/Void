from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<int:post_id>', views.detailedPostView, name="detailView"),
    path('get-post/<int:post_id>', views.getPost, name="detailPost"),
]