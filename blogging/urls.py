from django.urls import include, path
from rest_framework import routers

from blogging.views import PostListView, PostDetailView, PostViewSet

router = routers.DefaultRouter()
router.register(r"api/posts", PostViewSet)

urlpatterns = [
    path("", PostListView.as_view(), name=""),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
    path("api/posts", PostViewSet.as_view({"get": "list"}), name="post_api_view"),
]
