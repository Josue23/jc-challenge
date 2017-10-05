# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView
from .models import Candidate, Empresa, Vaga 
from django import forms
from .forms import CandidateForm


def home(request):
    return render(request, 'index.html')


class VagaCreate(CreateView):
    model = Vaga
    fields = ['name', 'empresa', 'min_salario',
                 'max_salario', 'experiencia', 'escolaridade', 'distancia']
    success_url = reverse_lazy('core:vaga_list')

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['name', 'description']
    success_url = reverse_lazy('core:empresa_list')
'''
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['name', 'description']
    success_url = reverse_lazy('core:empresa_list')
'''

def vaga_list(request):
    vagas = Vaga.objects.all()
    # forms = CandidateForm()
    ctx = {'vagas': vagas}
    return render(request, 'core/vaga_list.html', ctx)
    # return render(request, 'vaga_list')


def empresa_list(request):
    empresas = Vaga.objects.all()
    ctx = {'empresas': empresas}
    return render(request, 'core/empresa_list.html', ctx)


def login(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    kwargs['extra_context'] = {'next': reverse('home')}
    kwargs['template_name'] = 'login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('home')
    return logout(request, *args, **kwargs)


class RegistrationView(CreateView):
    #form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = "register.html"


def candidate_list(request):
    candidates = Candidate.objects.all()
    forms = CandidateForm()
    ctx = {'candidates': candidates, 'forms': forms}
    return render(request, 'core/candidate_list.html', ctx)


class CandidateCreate(CreateView):
    model = Candidate
    fields = ['username', 'first_name',
              'last_name', 'email', 'password', 'phone']
    success_url = reverse_lazy('core:candidate_list')


def candidate_edit(request, pk):
    if request.is_ajax() and request.method == 'POST':
        pk = request.POST.get('pk')
        candidate = get_object_or_404(Candidate, pk=pk)
        candidate.username = request.POST.get('username')
        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.email = request.POST.get('email')
        candidate.phone = request.POST.get('phone')
        candidate.password = request.POST.get('password')
        candidate.save()
        response = {'status': 'update'}
        return JsonResponse(response)
    else:
        return HttpResponseRedirect(reverse('core:candidate_list'))


def candidate_delete(request, pk):
    if request.is_ajax() and request.method == 'POST':
        pk = request.POST.get('pk')
        cand = Candidate.objects.get(pk=pk)
        cand.delete()
        response = {'status': 'Deletado com sucesso'}
        return JsonResponse(response)
    else:
        return HttpResponseRedirect(reverse_lazy('core:candidate_list'))
