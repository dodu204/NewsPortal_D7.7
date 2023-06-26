from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import News, Article
from .filters import NewsFilter, ArticleFilter


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'


class NewsCreateView(SuccessMessageMixin, CreateView):
    model = News
    template_name = 'news/news_create.html'
    fields = ['title', 'author', 'content']
    success_message = "New news article created successfully!"


class NewsUpdateView(SuccessMessageMixin, UpdateView):
    model = News
    template_name = 'news/news_update.html'
    fields = ['title', 'author', 'content']
    success_message = "News article updated successfully!"


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_list')
    success_message = "News article deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(NewsDeleteView, self).delete(request, *args, **kwargs)


class ArticleListView(ListView):
    model = Article
    template_name = 'news/article_list.html'
    context_object_name = 'article_list'
    paginate_by = 10


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'


class ArticleCreateView(SuccessMessageMixin, CreateView):
    model = Article
    template_name = 'news/article_create.html'
    fields = ['title', 'author', 'content']
    success_message = "New article created successfully!"


class ArticleUpdateView(SuccessMessageMixin, UpdateView):
    model = Article
    template_name = 'news/article_update.html'
    fields = ['title', 'author', 'content']
    success_message = "Article updated successfully!"


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'news/article_delete.html'
    success_url = reverse_lazy('article_list')
    success_message = "Article deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ArticleDeleteView, self).delete(request, *args, **kwargs)


class NewsSearchView(FilterView):
    filterset_class = NewsFilter
    template_name = 'news/news_search.html'
    paginate_by = 10
    context_object_name = 'filtered_news_list'
