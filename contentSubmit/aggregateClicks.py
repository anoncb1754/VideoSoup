from django.db import models
from clickTracker.models import ClicksTracked
from contentSubmit.models import Post



def aggregateClicks():
	posts = Post.objects.all()

	for post in posts:
		clicks = ClicksTracked.objects.filter(post_id=post.id).count()
		#Update click col in posts
		post.clicks = clicks
		post.save()