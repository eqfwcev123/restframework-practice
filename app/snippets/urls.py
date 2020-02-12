from django.urls import path

from snippets.apis.mixins import SnippetListCreateAPIView, SnippetRetrieveUpdateDestroyAPIView

app_name = 'snippets'
urlpatterns = [
    # path('snippets/', snippet_list),
    # path('snippets/<int:pk>/', snippet_detail)
    path('snippets/', SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>/', SnippetRetrieveUpdateDestroyAPIView.as_view()),
]
# as_view() 는 클래스 메서드이다. as_view()를 사용해서 클래스의 메소드를 생성한다.
# Function based View 는 함수를 호출해서 응답을 받는것이지만, 클래스의 호출은 인스턴스를 반환한다.
# 그렇기 때문에 as_view()를 사용하면 해당 클래스의 함수들을 생성한다는 뜻이다.
