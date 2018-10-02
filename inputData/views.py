from django.shortcuts import render
from django.http import HttpResponse
from inputData.models import ownerInfo

# Create your views here.
def index(request):
    return HttpResponse('欢迎光临')

def home(request):
    testList=map(str,range(100))
    return render(request,'home.html',{'string':testList})

def cmdt(request):
    return render(request,'commitData.html')

def cmtOk(request):
    roomNo=request.GET['roomNo']
    phoneNo=request.GET['phoneNo']
    ownerInfo.objects.get_or_create(roomNo=roomNo,phoneNo=phoneNo)
    return HttpResponse('提交成功,你提交的房号是'+roomNo+',你提交的手机号是'+phoneNo)
