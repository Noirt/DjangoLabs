from django.db import models
import datetime
# Create your models here.

class Author(models.Model):
	first_name = models.CharField('Name', max_length=30)
	last_name = models.CharField('Surname', max_length=30)
	email = models.EmailField(null = True, blank = True)

	def __unicode__(self):
		return '%s %s' % (self.last_name, self.first_name)

class Publisher(models.Model):
	title = models.CharField(max_length=32)
	address = models.TextField()
	city = models.CharField(max_length=64)
	country = models.CharField(max_length=64)
	website = models.URLField()

	def __unicode__(self):
	        return '%s (%s)' % (self.title, self.website)

class Book(models.Model):
	title = models.CharField(max_length=128)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField(default=datetime.datetime.now())

	def __unicode__(self):
		return self.title
