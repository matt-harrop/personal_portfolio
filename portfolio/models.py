from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    current = models.BooleanField(default=False)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    type = models.CharField(max_length=100, default="work")

    def __str__(self):
        return self.institution + " - " + self.title

    class Meta:
        ordering = ['-end_date']


class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    content = models.TextField()

    def __str__(self):
        elipses = "..." if len(self.content) > 50 else ""
        return self.first_name + " " + self.last_name + " | " + self.content[0: 50] + elipses

