# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView, CreateView
from .models import Candidate, Empresa, Vaga, CandidateChoice
from django import forms

CandidateForm = get_user_model()
User = get_user_model()

def home(request):
    return render(request, 'index.html')


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['name', 'description']
    success_url = reverse_lazy('core:empresa_list')


class VagaCreate(CreateView):
    model = Vaga
    fields = ['name', 'empresa', 'min_salario',
                 'max_salario', 'experiencia', 'escolaridade', 'distancia']
    success_url = reverse_lazy('core:vaga_list')


def vaga_list(request):
    vagas = Vaga.objects.all()
    ctx = {'vagas': vagas}
    return render(request, 'core/vaga_list.html', ctx)


class EscolhaCreate(CreateView):
    model = CandidateChoice
    fields = ['name', 'min_salario',
                 'max_salario', 'experiencia', 'escolaridade', 'distancia']
    success_url = reverse_lazy('core:escolha_list')


def escolha_list(request):
    escolhas = CandidateChoice.objects.all()
    # forms = CandidateForm()
    ctx = {'escolhas': escolhas}
    return render(request, 'core/escolha_list.html', ctx)
    # return render(request, 'vaga_list')


def empresa_list(request):
    empresas = Vaga.objects.all()
    ctx = {'empresas': empresas}
    return render(request, 'core/empresa_list.html', ctx)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('home')

'''
class RegisterView(CreateView):
    from_class = UserCreationForm
    template_name = 'register.html'
    model = User
    fields = '__all__'
    success_url =  reverse_lazy('login')
register = RegisterView.as_view()
'''
class RegisterView(CreateView):
    from_class = UserCreationForm
    template_name = 'register.html'
    model = User
    fields = ['email', 'password', 'password']
    success_url = reverse_lazy('login')
register = RegisterView.as_view()


class CandidateCreate(CreateView):
    model = Candidate
    fields = ['username', 'first_name',
              'last_name', 'email', 'password', 'phone']
    success_url = reverse_lazy('core:candidate_list')


def candidate_list(request):
    candidates = Candidate.objects.all()
    forms = CandidateForm()
    ctx = {'candidates': candidates, 'forms': forms}
    return render(request, 'core/candidate_list.html', ctx)


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
