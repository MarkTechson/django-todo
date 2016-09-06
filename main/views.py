from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Todo
from .forms import TodoForm

# Create your views here.
def list_todo(request):
	""" List of the todos created """
	todos = Todo.objects.all()
	context = {
		'todos': todos,
		'num_todos': todos.count,
		'form': TodoForm()
	}

	return render(request, 'list.html', context)


def add_todo(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.status = False
			todo.save()
			jsonResponse = JsonResponse({
				'message': 'Save Successful!',
				'title': todo.title,
				'pk': todo.pk
			})
		else:
			jsonResponse = JsonResponse({
				'message': 'Something went wrong, be sure to send a description'
			})
	else:
		jsonResponse = JsonResponse({
			'message': 'Unexpected Request'
		})

	return HttpResponse(jsonResponse, content_type='application/json')

def toggle_todo(request, id):
	if id:
		todo = get_object_or_404(Todo, pk=id)
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			form.save(commit=False)
			todo.status = not todo.status
			form.save()
			jsonResponse = JsonResponse({
				'message': 'Success!'
			})
	else:
		jsonResponse = JsonResponse({
			'message': 'Unexpected Request'
		})

	return HttpResponse(jsonResponse, content_type='application/json')

def update_todo(request, id):
	if id:
		todo = get_object_or_404(Todo, pk=id)
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			form.save()
			jsonResponse = JsonResponse({
				'message': 'Success!'
			})
	else:
		jsonResponse = JsonResponse({
			'message': 'Unexpected Request'
		})

	return HttpResponse(jsonResponse, content_type='application/json')

def delete_todo(request, id):
	if id:
		todo = get_object_or_404(Todo, pk=id)
		todo.delete()
		jsonResponse = JsonResponse({
			'message': 'Success!'
		})
	else:
		jsonResponse = JsonResponse({
			'message': 'Unexpected Request'
		})

	return HttpResponse(jsonResponse, content_type='application/json')
