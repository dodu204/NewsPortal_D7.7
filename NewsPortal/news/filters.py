from django_filters import FilterSet, CharFilter, DateFilter
from .models import News, Article


class NewsFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author', lookup_expr='icontains')
    min_date = DateFilter(field_name='pub_date', lookup_expr='gte')

    class Meta:
        model = News
        fields = ['title', 'author', 'min_date']


class ArticleFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author', lookup_expr='icontains')
    min_date = DateFilter(field_name='pub_date', lookup_expr='gte')

    class Meta:
        model = Article
        fields = ['title', 'author', 'min_date']
