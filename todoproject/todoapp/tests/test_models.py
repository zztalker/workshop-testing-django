from django.test import TestCase
from todoapp.models import TodoListItem

# Create your tests here.
class TodoListTest(TestCase):
    def test_can_create_a_todo_list_item(self):
        # Create a todo list item
        item = TodoListItem(content="This is a todo list item")
        # Save the todo list item to the database
        item.save()
        # Check we can find it
        all_items_in_database = TodoListItem.objects.all()
        self.assertEquals(len(all_items_in_database), 1)

        only_item_in_database = all_items_in_database[0]
        self.assertEquals(only_item_in_database, item)

        # Check attributes
        self.assertEquals(only_item_in_database.content, "This is a todo list item")

    def test_cant_create_todo_list_item_with_empty_content(self):
        # Create a todo list item with empty content
        item = TodoListItem(content="")
        # Try to save the todo list item to the database
        with self.assertRaises(Exception):
            item.save()
            item.full_clean()
