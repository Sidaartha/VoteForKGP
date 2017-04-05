from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	total_votes=models.IntegerField(default=0)

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	choice_text = models.CharField(max_length=200)
	image = models.FileField(null=True, blank=True)
	votes= models.IntegerField(default=0)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	percentage = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text