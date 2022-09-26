from django.shortcuts import render
from .models import  Post
# Create your views here.

def post_list(request):
    qs=Post.objects.all()
    q=request.GET.get('q','') #url 에서 q 라는 쿼리파라메터 값을 가져옴. defalut = ''s
    if q :
        qs = qs.filter(message__icontains=q)
    return render(request,'instagram/post_list.html',{'post_list':qs , 'bf_search' : q})

def post_detail(request,pk):
    pass