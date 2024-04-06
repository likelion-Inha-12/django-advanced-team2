import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import *



def create_member(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        id = data.get('id')
        email = data.get('email')
        is_leader = data.get('is_leader')
        hearts = data.get('hearts')

        member = Member(
            id = id,
            email = email,
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
    

    