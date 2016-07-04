"""ClientWeb urls."""

from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

app_name = "clientWeb"
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^accounts/profile/$', RedirectView.as_view(url='/')),
url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]
