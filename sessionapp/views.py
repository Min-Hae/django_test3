from django.shortcuts import render
from django.http.response import HttpResponseRedirect


# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def setosFunc(request):
    if 'favorite_os' in request.GET:
        #print(request.GET['favorite_os']) # favorite_os 이름의 인자를 받는다.
        request.session['f_os']= request.GET['favorite_os'] # request.GET['key값']으로 세션 읽고쓰기.
       # kbs =request.session['favorite_os'] = request.GET['favorite_os'] 로 변수를 할당할 수 있다.
       
        return HttpResponseRedirect('/showos') # showos 요청 발생
    else:
        return render(request, 'setos.html')
def showosFunc(request):
    context = {} # dict type
    if 'f_os' in request.session: # 세션 key 중에 f_os가 있을 때 실행
        context['dict_f_os'] = request.session['f_os'] # 세션 값 읽기 
        context['message'] = '당신이 선택한 운영체제는 %s'%request.session['f_os']
        
    else: # 세션에 값이 없을 때 실행
        context['dict_f_os'] = None
        context['message'] = '운영체제를 선택하지 못했네요'    
        
    request.session.set_expiry(5) # 5초 동안 클라이언트의 활동이 없으면 세션 삭제.
    return render(request, 'show.html', context)    