from django.conf.urls import url
from myproject.core import views as v
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^candidate/$', v.candidate_list, name='candidate_list'),
    url(r'^candidate/add/$', v.CandidateCreate.as_view(), name='candidate_add'),
    url(r'^candidate/(?P<pk>\d+)/edit/$',
        v.candidate_edit, name='candidate_edit'),
    url(r'^candidate/(?P<pk>\d+)/delete/$',
        v.candidate_delete, name='candidate_delete'),
]
