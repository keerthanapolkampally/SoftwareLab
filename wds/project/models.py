from django.db import models
from index.models import Profile

class project(models.Model):
	project_name = models.CharField(max_length=100)
	team_leader = models.CharField(max_length=100)
	employee = models.ManyToManyField(Profile)