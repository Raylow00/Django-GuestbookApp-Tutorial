from django.db import models
from django.utils import timezone

#create a model for the database
class Comment(models.Model):
    #for a comment, you need a name, the text comment and the date posted
    #ID is generated automatically
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.name, self.id)