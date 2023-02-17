from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog/images/")
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    author = models.CharField(max_length=255, null=True, blank=True)
    published_date = models.DateField()

