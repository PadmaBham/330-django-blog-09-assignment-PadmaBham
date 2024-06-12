from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from rest_framework import viewsets
from .serializers import PostSerializer


class PostListView(ListView):
    # context_object_name = "blog_index"
    queryset = Post.objects.exclude(published_date__isnull=True).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.exclude(published_date__isnull=True).order_by(
        "-published_date"
    )
    serializer_class = PostSerializer


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__isnull=True).order_by(
        "-published_date"
    )
    template_name = "blogging/detail.html"
