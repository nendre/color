import json, urllib2, base64
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

# Create your views here.
def start(request):
    return HttpResponse('<html><body>This is a test</body></html>', mimetype="text/html")
    
def moo(request):
    return HttpResponse('<html><body>This is moo</body></html>', mimetype="text/html")

def home(request):
    return render(request, "home.html")


def result(request):
    req = urllib2.urlopen('http://www.google.com')
    res = base64.b64encode(req.read())
    data = [res]
    return HttpResponse(json.dumps(data, indent=2), mimetype="text/json")
