from django.db import models
from django.contrib.auth.hashers import make_password # 비밀번호 암호화를 위한 함수


class Member(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)  # id 필드를 문자열로 선언하고, 기본 키로 설정합니다.
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()  # 이메일 필드
    password = models.CharField(max_length=128, default=make_password('default_password')) # 비밀번호 필드 추가
    is_leader = models.BooleanField(default=False)  # 팀 리더 여부, 기본값은 False
    hearts = models.IntegerField()  # 하트 수, 정수 필드

    # def toggle_leader(self):
    #     self.is_leader = not self.is_leader
    #     self.save()

# 모델 필드는 아래 링크 참고했습니다
# https://github.com/dkyou7/TIL/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC/Django/5.%20%5BDjango%5D%20Model%20%ED%95%84%EB%93%9C%ED%83%80%EC%9E%85%20%EC%A0%95%EB%A6%AC.md
