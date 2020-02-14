from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apis import generic, viewsets

router = DefaultRouter()
router.register(r'snippets', viewsets.SnippetViewSet)

app_name = 'snippets'
urlpatterns_api_view = [
    path('snippets/', generic.SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>/', generic.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]
# as_view() 는 클래스 메서드이다. as_view()를 사용해서 클래스의 메소드를 생성한다.
# Function based View 는 함수를 호출해서 응답을 받는것이지만, 클래스의 호출은 인스턴스를 반환한다.
# 그렇기 때문에 as_view()를 사용하면 해당 클래스의 함수들을 생성한다는 뜻이다.

urlpatterns_viewset = [
    # viewsets 을 이용할 때 actions을 지정해줘야 하는데
    # .as_view({ 'http_method' : 'viewset 함수들' }) 형식이다
    path('snippets/', viewsets.SnippetViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('snippets/<int:pk>/', viewsets.SnippetViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
    )),
]

urlpatterns = [
    path('api-view/', include(urlpatterns_api_view)),
    path('viewset/', include(urlpatterns_viewset)),
    path('router/', include(router.urls))
]
