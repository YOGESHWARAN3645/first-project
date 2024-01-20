
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
    
def home(request):
  template= loader.get_template('home.html')
  return HttpResponse(template.render())

def login(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('login.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  mydata = Member.objects.values_list('firstname')
  template = loader.get_template('query.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

def logindetails(request):
    username = request.GET["name"]
    password= request.GET["password"]
    return render(request,"logindetails.html",{'username':username,'password':password})
