from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    # model 생성날짜 자동저장
    updated = models.DateTimeField(auto_now=True)
    # model 변경날짜 자동저장

    class Meta:
        abstract = True

    # 데이터베이스지만 데이터베이스에 저장되지 않게. 다른 모델들만 활용하게 처리
