from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed

from .forms import PersonForm, TodoForm
from .models import Todo

# Create your views here.

def hello_world_view(req):
    return HttpResponse('Hello World')

def hello_python_view(req):
    return HttpResponse('Hello python')

def hello_html_view(req):
    return render(req, 'todos/hello.html')

def hello_path(req, name):
    return HttpResponse(f'Hello {name}')

def hello_query(req):
    return HttpResponse(f'Your query was {req.GET.get("q")}')

def special_view(req):
    return redirect('hello_html')

def post_example(req):
    if req.method == 'POST':
        form = PersonForm(req.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            job = form.cleaned_data['job']

        return HttpResponse(f'You posted: {name}, {age}, {job}')
    else:
       return HttpResponseNotAllowed('POST') 

def submit_example(req):
    return render(req, "todos/submit.html")

def submit_django_form(req):
    form = PersonForm()
    return render(req, "todos/submit_django_form.html", {'form': form})

def template_view(req):
    context = {
        "name": "Bob",
        "age": 5,
        "skills": ["Django", "SQL", "Docker"] 
    }
    
    return render(req, 'todos/template_demo.html', context)

def todos_view(req):
    if req.method == "POST":
        form = TodoForm(req.POST)
        
        if form.is_valid():
            todo = form.save()
            return HttpResponse('Todo successfully created!')
    else:
        form = TodoForm()
    
    todos = Todo.objects.all()

    return render(req, 'todos/todos.html', {'form': form, 'todos': todos})

