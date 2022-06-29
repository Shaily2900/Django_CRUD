from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistration
from .models import User
# Create your views here.

# This function will add new data and show all the data
def add_show(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg = User(name=nm, email=em, password = pw)
            reg.save()
            fm = UserRegistration()
    else:
        fm = UserRegistration()
    user = User.objects.all()
    return render(request,'myapp/add&show.html',{'form':fm, 'usr':user})

# This function will Update/Edit
def update_data(request, id):
    
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = UserRegistration(instance=pi)
    return render(request,'myapp/updateuser.html',{'form': fm })
        # return HttpResponseRedirect('/')


# This function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')