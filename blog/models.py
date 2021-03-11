from django.db import models
from datetime import date


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to='blog/images/')
    content = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title + ' - ' + str(self.date)
