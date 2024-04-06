from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_member),
    path('<int:pk>/', views.read_member),
    #path('update/<int:pk>/', views.update_member),
    #path('delete/<int:pk>/', views.delete_member),
    path('changePwd/<int:pk>/', views.change_password), #비밀번호 변경
    path('delete/<int:pk>/', views.delete_member), #회원 삭제
    path('pressHeart/<int:pk>/', views.press_heart), #하트 누르기
    path('leader/<int:pk>/', views.leader),
    path('list/', views.member_list)
]