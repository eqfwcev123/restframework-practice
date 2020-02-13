from rest_framework import viewsets

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

"""
Viewset class ia type fo class-based View, that does not provide any method handlers
such as .get() or .post(), and instead provides actions such as .list() or .creaate()

.get() 혹은 .post() 대신 .list() 혹은 .create() 제공

The method handlers for a ViewSet are only bound to the corresponding actions at the
point of finalizing the view, using the .as_view() method.
"""


class SnippetViewSet(viewsets.ModelViewSet):
    # ModelViewSet 이 GenericAPIView를 상속 받기 때문에 최소한 queryset과 serializer_class
    # 는 써줘야 한다.
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
