from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from datetime import datetime
from clickTracker.models import ClicksTracked

def clickTracker(request):
	'''
	Does click tracking on post urls
	'''

	destination = request.GET.get('dst')
	post_id = request.GET.get('id')
	timestamp = datetime.now()

	try:
		click = ClicksTracked(post_id=post_id, destination=destination, timestamp=str(timestamp))
		click.save()
	except DatabaseError:
		raise Http404
	
	try:
		return HttpResponseRedirect(destination)
	except:
		raise Http404

