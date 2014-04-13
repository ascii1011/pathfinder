from django.views.generic import ListView, DetailView
from .models import Campaign

class CampaignList(ListView):
    model = Campaign
    template_name='campaign/list.html'
    http_method_names = ['get',]
    paginate_by=25

class CampaignDetail(DetailView):
    model = Campaign
    template_name = 'campaign/detail.html'
    slug_field = 'slug'