from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import signUpForm


# Create your views here.
def signup(request):
    
    if(request.method == 'POST'):
        form = signUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account had been successfully created! You can log in below.')
            return redirect('login')

    else:    
        form = signUpForm()
    
    return render(request,'account/signup.html',{'form':form})
    