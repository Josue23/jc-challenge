from django.conf.urls import url
from myproject.core import views as v
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^$', v.home, name='home'),
    # url(r'^register/$', v.RegistrationView.as_view(), name="register"),
	url(r'^login/$', v.login_view, name="login"),
    url(r'^candidate/$', v.candidate_list, name='candidate_list'),
    url(r'^vaga/add/$', v.VagaCreate.as_view(), name='vaga_add'),
    url(r'^empresa/add/$', v.EmpresaCreate.as_view(), name='empresa_add'),
    url(r'^vaga/$', v.vaga_list, name='vaga_list'),
    url(r'^empresa/$', v.empresa_list, name='empresa_list'),
    url(r'^candidate/add/$', v.CandidateCreate.as_view(), name='candidate_add'),
    url(r'^candidate/(?P<pk>\d+)/edit/$', v.candidate_edit, name='candidate_edit'),
    url(r'^candidate/(?P<pk>\d+)/delete/$',
        v.candidate_delete, name='candidate_delete'),
]
