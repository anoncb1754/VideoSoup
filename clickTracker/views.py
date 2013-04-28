from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from datetime import datetime
from clickTracker.models import ClicksTracked
from contentSubmit.models import Post

def clickTracker(request):
	'''
	Does click tracking on post urls


	Next: Drop table for click tracker and sync it again with new schema
	'''

	post_id = request.GET.get('id')
	timestamp = datetime.now()
	try:
		post = Post.objects.get(id=post_id)
	except DatabaseError:
		raise Http404	
	try:
		click = ClicksTracked(post=post, destination=post.link, timestamp=str(timestamp))
		click.save()
	except DatabaseError:
		raise Http404
	try:
		return HttpResponseRedirect(post.link)
	except:
		raise Http404
	
