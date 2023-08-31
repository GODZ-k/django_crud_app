from pdb import post_mortem
from django.shortcuts import render,redirect
from django.http import HttpResponse
from employe.models import employe

def home(request):
    alldata=employe.objects.all()

    return render(request,'index.html',{'alldata':alldata})

def adddata(request):
    try:
     if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        info=request.POST.get('info')

        sendform=employe(name=name,email=email,phone=phone,info=info)
        sendform.save()
        return redirect('/')


    except:
      return redirect('adddata')

    return render(request,'adddata.html')

def delete(request,SNO):
      alldata=employe.objects.get(pk=SNO)
      alldata.delete()
      return redirect('/')

def update(request,SNO):
  ud=employe.objects.get(pk=SNO)
  return render(request,'update.html',{'ud':ud})

def do_update(request,SNO):
  if request.method=='POST':
    update_name=request.POST.get('name')
    update_email=request.POST.get('email')
    update_phone=request.POST.get('phone')
    update_info=request.POST.get('info')

    ud=employe.objects.get(pk=SNO)

    ud.name=update_name
    ud.email=update_email
    ud.phone=update_phone
    ud.info=update_info

    ud.save()
    return redirect('/')


