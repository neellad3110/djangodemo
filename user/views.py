from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import user_registration_form,user_authentication_form
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User 
from django.contrib import messages
# Create your views here.


def index(request):
    if request.user.is_authenticated :
        return redirect('home')
    else:
        return render(request,"user/index.html")

@login_required(login_url='/login')
def home(request):
    username = request.session.get('username')
    return render(request,"user/home.html",{'username': username})

         

def userlogout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('index-page')


def userregister(request):

    if request.user.is_authenticated :
        return redirect('home')
    else:       
        form = user_registration_form(request.POST) 
            # form object
        if request.method == 'POST':
            if form.is_valid():
                
                user_data=form.save()

                 #Authenticate the user
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    request.session['username'] = user_data.username 
                    return redirect('home') 

                
                

        else:
            form = user_registration_form()

        return render(request,"user/register.html",{'form':form})


def userlogin(request):

    if request.user.is_authenticated :
        return redirect('home')
    else:       
        form = user_authentication_form(request.POST) 

          
        if request.method == 'POST':
            
            if form.is_valid():

                username=form.cleaned_data.get('username_or_email')
                password=form.cleaned_data.get('password')

                if User.objects.filter(username=username).exists() or User.objects.filter(email=username).exists():

                    user_auth_username=authenticate(username=username, password=password)
                    user_auth_email=authenticate(email=username, password=password)
                    # check user mail and username

                    if user_auth_username is not None:
                        login(request, user_auth_username)
                        request.session['username'] = user_auth_username.username
                        messages.info(request, "You have been login successfully.") 
                        return redirect('home')

                    elif user_auth_email is not None:
                        login(request, user_auth_email)
                        user=User.objects.get(email=user_auth_email)
                        request.session['username'] = user.username
                        messages.info(request, "You have been login successfully.") 
                        return redirect('home')
                    
                    else :
                        messages.error(request,"Invalid username or password.")

                else:
                     messages.error(request,"User not exists!")         

            else:
                print(form.errors)   
                 

        else:
            form = user_authentication_form()
            

        return render(request,"user/login.html",{'form':form})
