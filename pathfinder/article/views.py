from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Article

class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'article/edit_article.html'

    def get_success_url(self):
        return reverse('article-list')

class ArticleCreate(CreateView):
    model = Article
    template_name = 'article/edit_article.html'

    def get_success_url(self):
        return reverse('article-list')

class ArticleList(ListView):
    model = Article
    http_method_names = ['get',]
    paginate_by=25

class ArticleDetail(DetailView):
    model = Article
    slug_field = 'slug'

