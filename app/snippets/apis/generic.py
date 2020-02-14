from rest_framework import generics, permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, SnippetCreateSerializer


# queryset = the queryset that should be used for returning objects from this view.
# serializer_class = The serializer class that should be used for validating and deserializing
# input, and for serializing output.

class SnippetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,  # READ 랑 RETRIEVE 만된다
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SnippetSerializer
        elif self.request.method == 'POST':
            return SnippetCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SnippetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
