from django.db import models

class TopSite(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='topsites/images/')

    def __str__(self):
        return self.name

