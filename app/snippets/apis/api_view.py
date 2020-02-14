import json

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetListCreateAPIView(APIView):
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 사용자가 입력한 데이터를 SnippetSerializer 에 넣어서 변환
        print(request.data)  # {'author': 1, 'title': '망고월드', 'code': "print('Mango world')"}
        print(type(request.data))  # <class 'dict'>
        print(json.dumps(request.data))  # {"author": 1, "title": "\ub9dd\uace0\uc6d4\ub4dc", "code": "print('Mango world')"}
        print(type(json.dumps(request.data)))  # <class 'str'>
        json_str = json.dumps(request.data)
        print(json.loads(json_str))  # {'author': 1, 'title': '망고월드', 'code': "print('Mango world')"}
        print(type(json.loads(json_str)))  # <class 'dict'>

        # 사용자가 보낸 데이터는 python data type 이다.이 데이터를 장고 데이터베이스에 저장해서 모델 인스턴스로 변경 해야함
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save()를 하기 전까지는 생성 업데이트가 되지 않는다.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Snippet, pk=pk)

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # APIView 내부에 dispatch 라는 애가 GET, PATCH, DELETE 를 소문자로 변경해서 그에 맞는게 HTTP method 에 있으면
    # 해당 HTTP 메소드를 실행 시킨다. 만약에 함수 이름을 dele 라고 오타를 낼 경우 DELETE 가 실행되지 않는다.
