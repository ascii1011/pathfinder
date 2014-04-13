from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token
from django.template.loader import render_to_string
from django.shortcuts import render_to_response

import json
from django.core.serializers.json import DjangoJSONEncoder

def render_it( request, template, vals=None ):     
    values = vals or {}
    return render_to_response( template, values, context_instance=RequestContext(request) )

def json_response(obj, convert=True):
    if convert:
        obj = json.dumps(obj, cls=DjangoJSONEncoder)
    return HttpResponse( obj, mimetype="application/javascript")

class dashboard(TemplateView):
    template_name = "index.html"
