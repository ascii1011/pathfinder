from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django import http
import json
from django.forms.models import model_to_dict

#import json
#from django.core.serializers.json import DjangoJSONEncoder

def render_it( request, template, vals=None ):     
    values = vals or {}
    return render_to_response( template, values, context_instance=RequestContext(request) )

#def json_response(obj, convert=True):
#    if convert:
#        obj = json.dumps(obj, cls=DjangoJSONEncoder)
#    return HttpResponse( obj, mimetype="application/javascript")

class dashboard(TemplateView):
    template_name = "index.html"



class JSONListResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.

        _objs = list()
        for _obj in context['object_list']:
            obj = dict()
            
            try:
                fields = self.fields
            except:
                fields = []

            for f in _obj._meta.fields:
                if fields and f.name in fields:
                    obj.update( {'%s' % str(f.name): '%s' % str(getattr(_obj, f.name)) })
                    try:
                        t = getattr(_obj, 'get_%s_display' % f.name)
                        obj.update( { '%s_display' % str(f.name): '%s' % str(t()) } )
                    except:
                        pass
            
            _objs.append( obj )

        return json.dumps(_objs)


