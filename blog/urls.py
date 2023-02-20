from django.urls import path
from .views import BlogListView, BlogDetail

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", BlogDetail.as_view(), name="blog_detail")
]