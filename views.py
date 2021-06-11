from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from django.shortcuts import render
from myapp.models import Task


def home(request):
    return render(request, 'home.html')


def index(request):
    context = {'success': False}
    if request.method == "POST":

        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(note_title=title, note_description=desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)


def tasks(request):
    allTasks = Task.objects.all()
    print(allTasks)
    context = {'tasks': allTasks}

    return render(request, 'tasks.html', context)


def list(request):
    mydictionary = {
        "allTasks": Task.objects.all()
    }
    return render(request, 'list.html', context=mydictionary)


def delete(request, id):
    obj = Task.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "allTasks": Task.objects.all()
    }
    return render(request, 'list.html', context=mydictionary)


def edit(request, id):
    obj = Task.objects.get(id=id)
    mydictionary = {
        "title": obj.title,
        "desc": obj.description,
        "priority": obj.priority,
        "id": obj.id
    }
    return render(request, 'edit.html', context=mydictionary)
