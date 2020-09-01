from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def mytimeline(request):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    context = {'myprofile': myprofile}
    return render(request, 'timeline/time-line.html', context)

def myabout(request):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    context = {'myprofile': myprofile, 'me': me}
    return render(request, 'timeline/about.html', context)

def updateprofile(request):
    me = request.user
    myprofile = Profile.objects.get(user=request.user)

    form = ProfileForm(request.POST or None, instance=myprofile)

    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('about')

    ppf = ProfilePic()
    cpf = CoverPic()

    if 'profile_image' in request.POST:
        ppf = ProfilePic(request.POST, request.FILES, instance=myprofile)
        if ppf.is_valid():
            ppf.save()
            return redirect('myupdate')

    if 'cover_image' in request.POST:
        cpf = CoverPic(request.POST, request.FILES, instance=myprofile)
        if cpf.is_valid():
            cpf.save()
            return redirect('myupdate')

    

    context = {'form': form, 'myprofile': myprofile, 'cpf': cpf, 'ppf': ppf}




    return render(request, 'timeline/edit-profile-basic.html', context)
