# Create your views here.
from django.shortcuts import render_to_response
def imprint(request):
	return render_to_response('impressum.html')

def privacyPolicy(request):
	return render_to_response('datenschutz.html')

def AGB(request):
	return render_to_response('agb.html')