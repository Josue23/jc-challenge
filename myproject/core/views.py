# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView
from .models import Candidate
from django import forms


def home(request):
    return render(request, 'index.html')


def candidate_list(request):
    candidates = Candidate.objects.all()
    ctx = {'candidates': candidates}
    return render(request, 'core/candidate_list.html', ctx)


class CandidateCreate(CreateView):
    model = Candidate
    fields = ['username', 'first_name',
              'last_name', 'email', 'password', 'phone']
    success_url = reverse_lazy('core:candidate_list')


def candidate_edit(request, pk):
    if request.is_ajax() and request.method == 'POST':
        pk = request.POST.get('candidate_edit_id')
        candidate = get_object_or_404(Candidate, pk=pk)
        # Usando instance não precisa pegar os campos um a um.
        # form = CandidateForm(request.POST, instance=candidate)

        # if not form.is_valid():
        #     error = {'error': form.errors}
        #     return JsonResponse(error, status=422)

        # contact.treatment = request.POST.get('treatment')
        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.email = request.POST.get('email')
        candidate.phone = request.POST.get('phone')
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
