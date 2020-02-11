from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'created']

    # # 데이터를 보낸다는 것은 2가지 의미를 갖는다
    # # 1. 새로운 데이터를 추가
    # # 2. 기존의 데이터를 업데이트
    # def create(self, validated_data):
    #     return Snippet.objects.create(**validated_data)
    #
    # # instance 는 python custom object 이다.
    # # validated data 는 update가 될 데이터
    # def update(self, instance, validated_data):
    #     for key, value in validated_data:
    #         setattr(instance, key, value)
    #         # instance.a = 'apple' 와 setattr(instance, a, 'apple') 와 동일
    #     instance.save()
    #     return instance
