from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    '''This is a serializer class which will be used to convert the data from the database to
    output data that we can then view.
    We will be using hyperlinks because we need to return some hyperlinks for the urls'''

    # read only so that it is not displayed when we are creating the object!
    url = serializers.ReadOnlyField() # the url's created will be hyperlinks so we inherit from that specific class

    class Meta:
        model = TodoItem
        fields = ('url', 'title', 'completed', 'order') # fields from the TodoItem class