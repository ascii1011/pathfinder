from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Traceroute

class TracerouteUpdate(UpdateView):
    model = Traceroute
    template_name = 'traceroute/edit_traceroute.html'

    def get_success_url(self):
        return reverse('traceroute-list')

class TracerouteCreate(CreateView):
    model = Traceroute
    template_name = 'traceroute/edit_traceroute.html'

    def get_success_url(self):
        return reverse('traceroute-list')

class TracerouteList(ListView):
    model = Traceroute
    http_method_names = ['get',]
    paginate_by=25

class TracerouteDetail(DetailView):
    model = Traceroute
    slug_field = 'slug'

