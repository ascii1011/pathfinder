from django.conf import settings
#from os.path import join as oj

def paths(request):
    return {
        'IMG_URL': "%simg/" % (settings.STATIC_URL),
        'CSS_URL': "%scss/" % (settings.STATIC_URL),
        'JS_URL': "%sjs/" % (settings.STATIC_URL),
        'PLUGINS_URL': '%splugins/' % settings.STATIC_URL,
        }