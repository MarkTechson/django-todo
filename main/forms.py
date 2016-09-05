from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TodoForm, self).__init__(*args, **kwargs)

		# add some classes to the form element
		self.fields['title'].widget.attrs = {
			'class': 'form-control input-lg',
			'placeholder': 'What needs to be done?'
		}

		self.fields['title'].widget.attrs['class'] = 'form-control input-lg'

	class Meta:
		model = Todo
		fields = ('title',)
		labels = {
			'title': ''
		}
