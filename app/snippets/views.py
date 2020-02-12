# Create your views here.
# csrf 는 django 가 template를 만들때 사용
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)  # safe=False 특수문자
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # serializer.data 는 파이썬 데이터인데 JsonResponse 가 파이썬 데이터를 JSON 형식으로 Render를 해준다.


# id에 접근하면 그에 해당하는 데이터 가져오기
@csrf_exempt
def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data, partial=True)  # partial=True 는 일부분만 업데이트 한다는 뜻이다.
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)  # 데이터를 지우기 때문에 화면에 표시할 JSON데이터가 없고
        # 그렇기 때문에 HttpResponse 를 사용
