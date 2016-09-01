from django.shortcuts import render
from .models import Todo

# Create your views here.
def list_todos(request):
	""" List of the todos created """
	todos = Todo.objects.all()
	context = {
		'todos': todos,
		'num_todos': todos.count
	}

	return render(request, 'list.html', context)