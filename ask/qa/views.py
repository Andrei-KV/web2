from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, Http404 
from .models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK wrong')

def head(request, *args, **kwargs):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 2)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    context = {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        }
    return render(request, "head.html", context)
