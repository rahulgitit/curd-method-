from django.shortcuts import render,redirect,HttpResponseRedirect
from enroll.forms import tododataForm
from enroll.models import databaseintodolist
# Create your views here.
def index(request):
    if request.method == "POST":
        form=tododataForm(request.POST)
        if form.is_valid():
            form.save()
            form=tododataForm()
    else:
        form=tododataForm()
    data=databaseintodolist.objects.all()
    return render(request,"index.html",{"form":form,"data":data})


def delete(request,id):
    if request.method == "POST":
        dt=databaseintodolist.objects.get(pk=id)
        dt.delete()
        return redirect('/home')
def edit(request,id):
    if request.method =="POST":
        dt=databaseintodolist.objects.get(pk=id)
        fm=tododataForm(request.POST, instance=dt)
        if fm.is_valid:
            fm.save()
            return redirect('/home')
    else:
        dt=databaseintodolist.objects.get(pk=id)
        fm=tododataForm(instance=dt)
    return render(request,'update.html',{"fm":fm})

