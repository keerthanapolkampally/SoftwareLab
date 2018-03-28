from django.db import models
from index.models import Profile

class project(models.Model):
	project_name = models.CharField(max_length=100)
	#team_leader = models.ForeignKey(Profile, on_delete = models.PROTECT)
	employee = models.ManyToManyField(Profile, blank = True, null = True)

	def __str__(self):
		return self.project_name