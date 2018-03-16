from django.conf.urls import url, include
from . import views

app_name = 'project'

urlpatterns = [
	url(r'^$',views.proj,name = "proj"),
	url(r'^add/$',views.ProjectCreate.as_view(),name="add"),
]