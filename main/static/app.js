/* global $ */
(function () {
	'use strict';

	$(document).ready(function () {
		var CSRF_TOKEN = $("[name='csrfmiddlewaretoken']").val();

		// Add a double click listener to all of the .todo-label elements
		// so that we can display an input form element when executed
		$('.todo-label').dblclick(function (e) {
			var id = getId($(e.currentTarget));
			var input = $('#' + createId(id, '-input')).toggleClass('hidden');
			var label = $('#' + createId(id, '-label')).toggleClass('hidden');
			// keep the text synced between both elements
			input.val(label.text());
		});

		// Add a key listener to respond to escape and enter. When these
		// are hit, submit the updated text for saving
		$('.todo-input').keydown(function (e) {
			if (e.which === 13 || e.which === 27) {
				e.preventDefault();
				var id = getId($(e.currentTarget));
				var input = $('#' + createId(id, '-input')).toggleClass('hidden');
				var label = $('#' + createId(id, '-label')).toggleClass('hidden');
				// update the original value
				if (input.val() !== '') {
					label.text(input.val());
					updateTodo(id);
				}
			}
		});

		// Add an onclick listener for completing elements, when clicked
		// the todo will toggle between status states
		$('.toggle-todo').click(function (e) {
			e.preventDefault();
			completeTodo(getId($(e.currentTarget)));
		});

		// Add an onclick listener for deleting elements, when clicked
		// the todo will be submitted for deletion by the server
		$('.delete-todo').click(function (e) {
			e.preventDefault();
			deleteTodo(getId($(e.currentTarget)));
		});


		// Adds a listener to the submit form to create a todo
		$('#add-todo').on('submit', function (e) {
			e.preventDefault();
			addTodo();
			return false;
		});


		function deleteTodo(id) {
			$.post('delete/' + id + '/', getPostData(id)).done(function () {
				// remove the element from the list
				$('#' + createId(id, '-row')).remove();
			});
		}

		function updateTodo(id) {
			$.post('update/' + id + '/', getPostData(id)).done(function () {});			
		}

		function completeTodo(id) {
			$.post('toggle/' + id + '/', getPostData(id)).done(function (data) {
				$('#' + createId(id, '')).toggleClass('fa-square-o fa-check-square-o');
				$('#' + createId(id, '-label')).toggleClass('completed');
			});
		}

		function addTodo() {
			$.post('add/', $('#add-todo').serialize()).done(function (data) {
				// Since the post was successful, then let's clear out the form
				$('#add-todo :input[type=text]').val('');
				// Add the new element to the list
				$('.todo-list-section').append('<div class="todo">' + data.title + '</div>');
			});
		}

		/* Utility Functions */
		function getPostData(id) {
			return 'csrfmiddlewaretoken=' + CSRF_TOKEN + '&title=' + $('#' + createId(id, '-label')).text().replace(/ /g, '+');
		}

		function createId(id, suffix) {
			return '__' + id + suffix;
		}

		function getId(element) {
			return element.attr('id').split('-')[0].replace(/_/g, '');
		}
	});
})();