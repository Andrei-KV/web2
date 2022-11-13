from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, Http404 
from .models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK wrong')

def head(request, *args, **kwargs):
    questions = Question.objects.new()
    query_p = request.GET['page']
    limit = request.GET.get('limit', 1)
    page = request.GET.get('page', query_p)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    print(page)
    context = {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        }
    return render(request, "head.html", context)
