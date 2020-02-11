from django.db import models

# Create your models here.

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    # created = models.DateTimeField(auto_now_add=True, db_index=True) # DB index설정(Field.db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=50)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=50)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]
        # 정렬은 아주 비싼 연산 이기 때문에 인덱스 처리를 해줘야한다. (효율적)
        # 단점 : 만약에 수많은 데이터 사이에 새로운 데이터를 넣게될 경우 문제가 생긴다
