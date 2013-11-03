from django.db import models
#from mx.DateTime import Timezone

import datetime
from django.utils import timezone


# Create your models here.
# polls is an app

#each question has the text & a publication date
class Question(models.Model): #inherit from models.Model
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True #inputs a green check image
    was_published_recently.short_description = 'Published recently?'

#each choice relates to a question, has a choice text, and allows for votes
class Choice(models.Model):
    question = models.ForeignKey(Question) #related to the question class
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text