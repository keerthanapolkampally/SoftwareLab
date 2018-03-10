ffrom django.conf.urls import url
from . import views as index_views

urlpatterns = [
    ...
    url(r'^signup/$', index_views.signup, name='signup'),
]