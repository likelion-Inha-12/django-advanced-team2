from django.db import models

class Post(models.Model):
    # id는 자동으로 생성해 준다해서 적지 않았습니다!
    email = models.EmailField()
    is_leader = models.BooleanField(default = False)
    hearts = models.IntegerField(default = 0)

# 모델 필드는 아래 링크 참고했습니다
# https://github.com/dkyou7/TIL/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC/Django/5.%20%5BDjango%5D%20Model%20%ED%95%84%EB%93%9C%ED%83%80%EC%9E%85%20%EC%A0%95%EB%A6%AC.md
