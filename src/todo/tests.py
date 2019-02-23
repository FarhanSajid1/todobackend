from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import TodoItem
from django.urls import reverse

# Create your tests here.
def createItem(client):
    '''This performs the check of creating an item'''
    url = reverse('todoitem-list')
    data = {'title' : 'Walk the dog'}
    return client.post(url,data,format='json')

class TestCreateTodoItem(APITestCase):
    def setUp(self):
        self.response = createItem(self.client)

    def test_received_201_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_item_was_created(self):
        self.assertEqual(TodoItem.objects.count(), 1)

    def test_item_has_correct_title(self):
        self.assertEqual(TodoItem.objects.get().title, 'Walk the dog')


class TestUpdateTodoItem(APITestCase):
    '''Ensure that we can update an existing todo item using put '''
    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(TodoItem.objects.get().completed, False) # check to see that the item is false
        url = response['Location'] # the response location is stored in the response
        data = {'title': 'Walk the dog', 'completed': True}
        self.response = self.client.put(url, data, format='json') # put response for uploading

    def test_received_200_created(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_updated(self):
        '''If this returns true that means that the object was sucessfully updated'''
        self.assertEqual(TodoItem.objects.get().completed, True)

class TestDeleteTodoItem(APITestCase):
    '''Delete a single todo item'''
    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(TodoItem.objects.count(), 1)
        url = response['Location']
        self.response = self.client.delete(url) # deleting the url

    def test_recieved_204_not_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_the_item_was_deleted(self):
        self.assertEqual(TodoItem.objects.count(), 0)


class TestDeleteAllItmes(APITestCase):
    '''Ensure delete of all todo items'''

    def setUp(self):
        createItem(self.client)
        createItem(self.client)
        self.assertEqual(TodoItem.objects.count(), 2)
        self.response = self.client.delete(reverse('todoitem-list'))

    def test_recieved_204_not_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_all_items_were_deleted(self):
        self.assertEqual(TodoItem.objects.count(), 0)