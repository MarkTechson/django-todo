# Django Todo (django_todo)
A todo mvc esque implementation using Django 1.10 / Python 3

## Getting Started
* Clone this repository
* run ```python manage.py migrate``` to create the db and apply migrations
* run ```python manage.py runserver``` command and it will start the server. 

Finally, Visit ```http://localhost:8000``` to view the main page.

Todos can be created, completed, edited and deleted in this implementation. The communication is based on Ajax priciples and uses JQuery to help with the DOM manipulation.

## The Stack
* Django 1.10
* Python 3
* JQuery
* Font Awesome
* Bootstrap

## Known Issues
* When performing an operation, no loading screen is used
* Error handling can be improved
