# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from contentSubmit.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from clickTracker.models import ClicksTracked 
from django.db import connection

CONTACTS_PER_PAGE = 20	




def mostClicked(request):
	results = Post.objects.filter(status='Online').order_by('-clicks')
	page = request.GET.get('page')
	label_set = makeLabelSet(results)
	paginator = Paginator(zip(results, label_set), CONTACTS_PER_PAGE)

	sub_title = 'Meist geklickte Links'

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return render_to_response('index.html', {'posts': posts,
											'label_set': label_set,
											'sub_title': sub_title})



def category(request):
	category = request.GET.get('catid')
	
	if category:
		category = request.GET.get('catid').lower()
	page = request.GET.get('page')
	sub_title = category
	label = category
	print 'CATGORY', category

	if category == "sonstige":
		results = Post.objects.filter(status='Online').order_by('-date_created').exclude(
			Q(labels__contains='ard') | Q(labels__contains='zdf') | Q(labels__contains='arte')
			| Q(labels__contains='youtube'))
			
	else:
		results = Post.objects.filter(status='Online').order_by('-date_created').filter(labels__contains=label)
	label_set = makeLabelSet(results)
	paginator = Paginator(zip(results, label_set), CONTACTS_PER_PAGE)



	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return render_to_response('index.html', {'posts': posts,
											'label_set': label_set,
											'sub_title': sub_title,
											'catid': category})
	


def latest(request):
	'''
	Get the latest posts in the database that can be published
	indicated by status 'Online'.
	Then create a paginator object that paginages all the results and 
	returns the paginator to be rendered in the given template.
	'''
	results = Post.objects.filter(status='Online').order_by('-date_created')
	page = request.GET.get('page')
	label_set = makeLabelSet(results)
	paginator = Paginator(zip(results, label_set), CONTACTS_PER_PAGE)

	sub_title = 'Neueste Videos'

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return render_to_response('index.html', {'posts': posts,
											'label_set': label_set,
											'sub_title': sub_title})


def filterByLabel(request):
	label = request.GET.get('label')
	sub_title = 'Label Filter: ' + label
	
	 # Show 10 contacts per page
	page = request.GET.get('page')
	
	results = Post.objects.filter(status='Online').order_by('-date_created').filter(labels__contains=label)
	label_set = makeLabelSet(results)
	paginator = Paginator(zip(results, label_set), CONTACTS_PER_PAGE)

	print 'REQUEST', request.get_full_path()
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return render_to_response('index.html', {'posts': posts,
											'label_set': label_set,
											'sub_title': sub_title,
											'label': label})


'''
Helpers
'''
def enumarateRanks(num_ranks):
	ranks = []
	for i in range(1, num_ranks):
		ranks.append(i)

	return ranks

def makeLabelSet(results):
	label_set = []
	for item in results:
		labels = item.labels.replace(" ", "").split(',')
		label_set.append(labels)

	print label_set
	return label_set