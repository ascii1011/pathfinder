from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Source

class SourceUpdate(UpdateView):
    model = Source
    template_name = 'source/edit_source.html'

    def get_success_url(self):
        return reverse('source-list')

class SourceCreate(CreateView):
    model = Source
    template_name = 'source/edit_source.html'

    def get_success_url(self):
        return reverse('source-list')

class SourceList(ListView):
    model = Source
    http_method_names = ['get',]
    paginate_by=25

class SourceDetail(DetailView):
    model = Source
    slug_field = 'slug'
