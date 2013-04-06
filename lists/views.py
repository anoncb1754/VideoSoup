# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from contentSubmit.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def latest(request):
	'''
	Get the latest posts in the database that can be published
	indicated by status 'Online'.
	Then create a paginator object that paginages all the results and 
	returns the paginator to be rendered in the given template.
	'''
	results = Post.objects.filter(status='Online').order_by('-date_created')
	contacts_per_page = 20
	paginator = Paginator(results, contacts_per_page) # Show 10 contacts per page
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return render_to_response('index.html', {'posts': posts})


def enumarateRanks(num_ranks):
	ranks = []
	for i in range(1, num_ranks):
		ranks.append(i)

	return ranks