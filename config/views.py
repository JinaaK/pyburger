# -*- coding:utf-8 -*-
#주문을 처리하는 직원
#백엔드 영역

from django.http import HttpResponse

def main(request):
    return HttpResponse("안녕하세요, pyburger입니다.")

def burger_list(request):
    return HttpResponse("pyburger의 햄버거 목록입니다")