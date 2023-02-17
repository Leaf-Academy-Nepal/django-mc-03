from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class WorkExperience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_currently_working = models.BooleanField(default=False)
    