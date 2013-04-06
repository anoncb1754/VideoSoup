# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from contentSubmit.forms import SubmitForm
from contentSubmit.models import Post
from django.core.context_processors import csrf
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate
import urllib2


'''
todo:


-Design & Layout
-Label Management: Make all labels lowercase (DONE)

Put all labels into a table called labels,
Check if label already exists, if not then insert into db table. Call label using foreign key.
Display with bootstrap badges.

MAke all labels linked 

-Ranks & Sorting -->DONE

-Paginator for start page --> DONE
-activate Admin page --> DONE
-AGB, Datenschutz etc.


--> Release 0.1

-Submit by users 
-User login and registration
--Registration
--Post Manager for User
--Request content from url via python or js
--Check if url is okay.

--> Release 0.2

--Ranking algorithm
--simple blog

-->Release 0.3
--YouTube API bot
--ZDF bot
--ARD bot
--ContentManagerBot

'''


def contentSubmit(request):
	'''
	View for submitting content to the database.
	'''
	user = authenticate(username='cb1754', password='PeterBerg')
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		form = SubmitForm(request.POST)
		if form.is_valid():
			print 'Submitted'
			print request.user
			print request.POST.get('title')
			print datetime.now()
			post = Post(user = user, title=request.POST.get('title'),
				link=request.POST.get('link'),
				labels=request.POST.get('labels'),
				status=request.POST.get('status'),
				date_created=str(datetime.now()))
			post.save()
			return HttpResponseRedirect("/front_page")
	else:
		form = SubmitForm()

	return render(request,'content_submit.html',
			{'form': form})


def frontPage(request):
	results = Post.objects.filter(status='Online').order_by('-date_created')
	paginator = Paginator(results, 10) # Show 25 contacts per page
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


def manageContent(request):
	'''
	Query all posts with all states of the user.
	And display in post overview page.
	'''
	user = authenticate(username='cb1754', password='PeterBerg')
	print user
	my_posts = Post.objects.filter(user=user)
	print my_posts
	return HttpResponse('ManageContent')

def _getContentFromURL():
	pass
