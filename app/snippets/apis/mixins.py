from rest_framework import generics, mixins

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetListCreateAPIView(mixins.ListModelMixin, generics.GenericAPIView, mixins.CreateModelMixin):
    # generics :  같은 부분의 로직을 써놓고 다른 부분은 따로 쓰는 방식. 만약에 Snippets.objects.all() 와 Post.objects.all()이 있으면
    # 전체적인 로직은 같지만 model 와 serializer 만 다른것이다

    # Model
    # Serializer
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # ListModelMixin 내부의 list 메소드
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # CreateModelMixin 내부의 create 메소드
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                          generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
