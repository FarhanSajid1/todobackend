from django.shortcuts import render
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework import viewsets, status
from rest_framework.reverse import reverse
from rest_framework.response import Response

# Create your views here.
'''This is going to construct the view for the '''
class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all() # returns all the queries
    serializer_class = TodoItemSerializer

    def perform_create(self, serializer):
        '''This is a get request which creates a serializer and then generates a url to be saved '''
        instance = serializer.save()

        # this code creates a url as the following http://localhost/todos/pk
        # generate a hyperlink
        instance.url = reverse('todoitem-detail', args=[instance.pk], request=self.request)
        instance.save()

    def delete(self, request):
        '''This deletes all the requests'''
        TodoItem.objects.all().delete() # this deletes all the objects
        return Response(status = status.HTTP_204_NO_CONTENT)

