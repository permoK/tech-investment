# authapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# from .forms import SignUpForm
from django.http import HttpResponse, request, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import get_user_model


# import models
from .models import UserProfile, UserAccount

# import forms
from .forms import CreateUserForm, UserProfileForm, loginForm, reset_passwordForm, deposit_form, withdraw_form, searchForm, StkpushForm

# Create your views here.

#Admin
# @login_required(login_url='login')
def adminLogin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # authenticate user
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('adminDashboard')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('admin-login')
    else:
        form = loginForm()
    return render(request, 'admin/admin_login.html', {'form': form, 'messages': messages.get_messages(request)})

def adminDashboard(request):
    message = messages.get_messages(request)
    context = {'message':message, 'products': [100, 200, 30, 40, 500]}
    return render(request, 'admin/adminDashboard.html', context)

def admin_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    
    return redirect('admin_login')

def admin_users(request):
    return render(request, 'admin_users.html')

def admin_workplace(request):
    return render(request, 'admin_workplace.html')

#users
def dashboard(request):
    return render(request, 'dashboard.html')

def users(request):
    return render(request, 'users.html')

def user_profile(request):
    user_transactions = []
    user_deposit = []
    user_withdraw = []
    user_assets = []
    user_balance = []

    return render(request, 'user_profile.html')



#authentications
def login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # authenticate user
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('adminDashboard')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')
    else:
        form = loginForm()

    message = messages.get_messages(request)
    return render(request, 'auth/login.html', {'form': form, 'messages': message})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = UserProfile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
    except:
        pass

    profile_id = request.session.get('ref_profile')
    print('profile_id', profile_id)

    
    form = CreateUserForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            #save the user
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            if profile_id is not None:
                recommender_id = UserProfile.objects.get(id=profile_id)
                recommender_username = recommender_id.username
                #save the user
                user = form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                # create user instance
                User_instance = User.objects.get(username=recommender_username)
                # create a recommendation instance
                profile_instance = UserProfile.objects.get(username=user.username)

                # set the user instance as the recommender
                profile_instance.recommended_by = User_instance
                # save the profile
                profile_instance.save()

                # add the user to the recommender's list of recommended users
                # User_instance.recommended.add(profile_instance)
                # save the user
                # User_instance.save()
                
                # clear the session
                del request.session['ref_profile']


            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Redirect to your login page

    else:
        # form error
        form = CreateUserForm()
        profile_form = UserProfileForm()
        context = { "form":form, "profile_form":profile_form, "errors":form.errors, "errors":profile_form.errors}
    context = { "form":form, "profile_form":profile_form, "errors":form.errors, "profile_errors":profile_form.errors }

    return render(request, 'auth/register.html', context)

def reset_password(request):
    return render(request, 'auth/reset_password.html')

def reset_confirm(request):
    return render(request, 'reset_confirm.html')

def reset_complete(request):
    return render(request, 'reset_complete.html')

def reset_done(request):
    return render(request, 'reset_done.html')



#transactions
def transactions_history(request):
    return render(request, 'transactions_history.html')

def transactions_pending(request):
    return render(request, 'transactions_pending.html')

def transactions_completed(request):
    return render(request, 'transactions_completed.html')

def deposit(request):
    return render(request, 'deposit.html')

def withdraw(request):
    return render(request, 'withdraw.html')

#assets
def assets(request):
    return render(request, 'assets.html')

def recommended_users(request):
    profile = []
    for prof in UserProfile.objects.all():
        if prof.recommended_by == request.user:
            profile.append(prof)
        #count the number of recommended users
    recommended_users = len(profile)
    return HttpResponse('recommended_users: ' + str(recommended_users))


#ajax requests
def get_chart_data(request):
    # Replace this with your actual logic to fetch updated data
    updated_data = [12, 99, 0, 6, 70]
    return JsonResponse({'data': updated_data})


