import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import *


def create_member(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        id = data.get('id')
        email = data.get('email')
        password = data.get('password')
        is_leader = data.get('is_leader')
        hearts = data.get('hearts')

        member = Member(
            id = id,
            email = email,
            password = password,
            is_leader = is_leader,
            hearts = hearts
        )
        member.save()
        return JsonResponse({'message':'success'})
     
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})

def read_member(request, pk):
    if request.method == 'GET':
        # get_object_or_404 함수를 사용하여 member 객체를 가져옵니다.
        # 객체가 존재하지 않는 경우, 404 에러를 반환합니다.
        member = get_object_or_404(Member, id=pk)
        
        # member 객체에서 필요한 정보를 추출하여 data 딕셔너리를 구성합니다.
        data = {
            'id': member.id,
            'email': member.email,
            'is_leader': member.is_leader,
            'hearts': member.hearts,
        }
        
        return JsonResponse(data, status=200)
    else:
        # GET 요청이 아닌 경우, 405 Method Not Allowed 에러를 반환합니다.
        return JsonResponse({'message': 'GET 요청만 허용됩니다.'}, status=405)
    

#기능3 : 회원 정보 수정(특정 id의 비밀번호 수정 기능)
def change_password(request, pk):
    if request.method == 'PATCH':
        member = get_object_or_404(Member, pk=pk)
        data = json.loads(request.body)
        new_password = data.get('new_password')

        if new_password:
            member.password = new_password  # 비밀번호 변경
            member.save() # 변경사항 저장
            return JsonResponse({'message': 'Password updated success. noew_password :'+ new_password}, status=200)
        else:
            return JsonResponse({'message': 'New password not provided'}, status=400)
    else:
        return JsonResponse({'message': 'PATCH 요청만 허용됩니다.'}, status=405)

#기능4 : 사용자 삭제 기능
def delete_member(request, pk):
    if request.method == 'DELETE':
        member = get_object_or_404(Member, id=pk)
        member.delete()
        return JsonResponse({'message': 'success'}, status=200)
    else:
        return JsonResponse({'message': 'DELETE 요청만 허용됩니다.'}, status=405)

#기능5 : 하트 누르기 기능
def press_heart(request, pk):
    if request.method == 'PATCH':
        member = get_object_or_404(Member, id=pk)
        member.hearts += 1  # 하트 수를 1 증가
        member.save()
        return JsonResponse({'message': f'{pk}의 총 하트 수는 {member.hearts}입니다.'})
    else:
        return JsonResponse({'message':'PATCH 요청만 허용됩니다.'})


def leader(request, pk):
    if request.method == 'POST':
        member = get_object_or_404(Member, id=pk)

        if member.is_leader == True:
            member.is_leader = False
            member.save()
            return JsonResponse({'message': f'{pk}의 대표 자격을 박탈 하였습니다.'})
        else:
            for leader_member in get_list_or_404(Member):
                if leader_member.is_leader == True:
                    return JsonResponse({'message':'대표는 2명이상일 수 없습니다.'}, status=400)
            
            member.is_leader = True
            member.save()
            return JsonResponse({'message': f'{pk}를 대표로 임명 하였습니다.'})
    else:
        return JsonResponse({'message':'POST 요청만 허용됩니다.'})



def member_list(request):
    if request.method == 'GET':
        member_count = 0
        total_hearts = 0
        for member in get_list_or_404(Member):
            member_count += 1
            total_hearts += member.hearts

        data = {
            'message' : "총 회원 수와 총 하트 수",
            'member_count' : member_count,
            'total_hearts' : total_hearts
        }
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({'message':'GET 요청만 허용됩니다.'}, status=405)
