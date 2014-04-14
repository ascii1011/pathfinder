from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Campaign

class CampaignUpdate(UpdateView):
    model = Campaign
    template_name = 'campaign/edit_campaign.html'

    def get_success_url(self):
        return reverse('campaign-list')

class CampaignCreate(CreateView):
    model = Campaign
    template_name = 'campaign/edit_campaign.html'

    def get_success_url(self):
        return reverse('campaign-list')

class CampaignList(ListView):
    model = Campaign
    http_method_names = ['get',]
    paginate_by=25

class CampaignDetail(DetailView):
    model = Campaign
    slug_field = 'slug'

