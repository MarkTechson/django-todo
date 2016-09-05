from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todos(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)

		if form.is_valid():
			todo = form.save(commit=False);
			todo.completed = False;
			todo.save();

	# Get the create the context object
	# to be sent to the UI
	""" List of the todos created """
	todos = Todo.objects.all()

	context = {
		'todos': todos,
		'num_todos': todos.count,
		'form': TodoForm()
	}

	return render(request, 'list.html', context)