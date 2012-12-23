from django.db import models

# Create your models here.

class StoredData(models.Model):
	name = models.CharField(max_length = 6)
	date = models.DateField()

	def __unicode__(self):
		return '%s %s' % (self.name, self.date)
