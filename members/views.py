
from .models import Member
from django.shortcuts import render

def members(request):
  mymembers = Member.objects.all().values()
  context = {'mymembers': mymembers,}
  return render(request,'all_members.html',context)

def details(request, id):
  mymember = Member.objects.get(id=id)
  context = {
    'mymember': mymember,
  }
  return render(request,'details.html',context)

def home(request):
  return render(request,'home.html')

def login(request):
  mymembers = Member.objects.all().values()
  context = {'mymembers': mymembers,}
  return render(request,'login.html',context)

def testing(request):
  mydata = Member.objects.values_list('firstname')
  context = {
    'mymembers': mydata,
  }
  return render(request,'query.html',context)

def logindetails(request):
    username = request.GET["name"]
    password= request.GET["password"]
    return render(request,"logindetails.html",{'username':username,'password':password})
