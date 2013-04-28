from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

'''
@todo: just auto incremeny field for clicks
'''
class Post(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=255)
	link = models.URLField()
	labels = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	date_created = models.DateTimeField()
	clicks = models.PositiveIntegerField()

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		#Save all labels in lowercase format
		self.labels = self.labels.lower()
		super(Post, self).save()


	
# Create your models here.
