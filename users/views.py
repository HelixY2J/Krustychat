from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from .forms import *

def profile_views(request,username=None):
    if username:
         profile = get_object_or_404(User,username=username).profile
    else:
         try:
              profile = request.user.profile # if profile page is requested when logged out

         except:
              return redirect('account_login') # redirect user to login page first
    
    return render(request,'users/profile.html',{'profile':profile})

@login_required
def profile_edit_view(request):
    form = profileForm(instance=request.user.profile)

    if request.method == 'POST':
        form = profileForm(request.POST,request.FILES,instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
        
    if request.path == reverse('profile-onboarding'):
            onboarding = True
    else:
         onboarding = False




    return render(request,'users/profile_edit.html',{'form':form ,'onboarding':onboarding})


@login_required
def profil_settings_view(request):
     return render(request,'users/profile_settings.html')


@login_required
def profile_emailchange(request):
     if request.htmx:
          form = EmailForm(instance=request.user)
          return render(request,'partials/email_form.html',{'form':form})
     

     if request.method == 'POST':
          form = EmailForm(request.POST, instance=request.user)

          if form.valid():

               #chceking if the email already exists
               email = form.cleaned_data['email']
               if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                    messages.warning(request,f'{email} is already in use man')
                    return redirect('profile-settings')

               form.save()

               # signal updates emailaddresss and set verified to false

               send_email_confirmation(request,request.user )

               return redirect('profile-settings')
          else:
               messages.warning(request,'Form is not valid')
               return redirect('profile-settings')
     
     
     return redirect('home')