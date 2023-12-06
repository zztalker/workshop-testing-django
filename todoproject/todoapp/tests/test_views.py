from django.test import TestCase, Client
from todoapp.views import todoappView, addTodoView, deleteTodoView
from todoapp.models import TodoListItem


class TodoListTest(TestCase):
    def test_add_todo(self):
        client = Client()
        response = client.post('/addTodoItem/', {'content': 'This is a todo list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/todoapp/')
        all_items_in_database = TodoListItem.objects.all()
        self.assertEqual(len(all_items_in_database), 1)
        only_item_in_database = all_items_in_database[0]
        self.assertEqual(only_item_in_database.content, "This is a todo list item")

    def test_delete_todo(self):
        item = TodoListItem(content="This is a todo list item")
        item.save()
        all_items_in_database = TodoListItem.objects.all()
        self.assertEqual(len(all_items_in_database), 1)
        client = Client()
        response = client.post('/deleteTodoItem/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/todoapp/')
        all_items_in_database = TodoListItem.objects.all()
        self.assertEqual(len(all_items_in_database), 0)
