from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from datetime import datetime
from clickTracker.models import ClicksTracked
from contentSubmit.models import Post

def clickTracker(request):
	post_id = request.GET.get('id')
	timestamp = datetime.now()
	
	post = Post.objects.get(id=post_id)
	
	try:
		raw_click = ClicksTracked(post=post, destination=post.link, timestamp=str(timestamp))
		raw_click.save()
		post.clicks+=1
		post.save()
	except DatabaseError:
		raise Http404
	try:
		return HttpResponseRedirect(post.link)
	except:
		raise Http404
	
	
