import json
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt
from pathfinder.views import JSONResponseMixin
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


class CampList(JSONResponseMixin, ListView):
    model = Campaign
    http_method_names = ['get',]

@csrf_exempt
def CampaignDelete(request):
    data = {'result': 0}
    #print 'campaign delete'
    if request.method == 'POST':
        #print 'post!'
        from pprint import pprint
        pprint( request.POST.get('slug') )
        campaign = Campaign.objects.get(slug=request.POST.get('slug'))
        campaign.delete()

        data['result'] = 1
        response = HttpResponse(json.dumps(data))
        response['status'] = 200
        return response

    #print 'GET!!'

    return HttpResponseNotAllowed(['GET',])
