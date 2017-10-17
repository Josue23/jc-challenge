from django.conf.urls import url
from myproject.core import views as v
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^$', v.home, name='home'),

    url(r'^vaga/add/$', v.VagaCreate.as_view(), name='vaga_add'),
    url(r'^vaga/$', v.vaga_list, name='vaga_list'),

    url(r'^empresa/add/$', v.EmpresaCreate.as_view(), name='empresa_add'),
    url(r'^empresa/$', v.empresa_list, name='empresa_list'),

    url(r'^escolha/add/$', v.EscolhaCreate.as_view(), name='escolha_add'),
    url(r'^escolha/$', v.escolha_list, name='escolha_list'),

    url(r'^candidate/add/$', v.CandidateCreate.as_view(), name='candidate_add'),
    url(r'^candidate/$', v.candidate_list, name='candidate_list'),
    url(r'^candidate/(?P<pk>\d+)/edit/$', v.candidate_edit, name='candidate_edit'),
    url(r'^candidate/(?P<pk>\d+)/delete/$',
        v.candidate_delete, name='candidate_delete'),

]
