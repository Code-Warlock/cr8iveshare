from django.contrib.auth import authenticate, login, logout as logoutUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect

from accounts.forms import AccountAuthenticationForm, AccountUpdateForm, RegistrationForm
from accounts.models import Account, Profile
# from django.utils.http import is_safe_url


def register(request):
    template_name = 'accounts/register.html'
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            # create a profile object for the new user
            user_model = Account.objects.get(username=username)
            new_profile = Profile.objects.create(
                user=user_model, id_user=user_model.id)
            new_profile.save()
            messages.success(request, 'User registered successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
            context = {"signupform": form}
    else:  # GET Request
        form = RegistrationForm()
        context = {"signupform": form}
    return render(request, template_name, context)


def login_view(request):
    template_name = 'accounts/login.html'
    form = AccountAuthenticationForm()

    user = request.user
    if user.is_authenticated:
        return redirect('/')
    if request.POST:
        form = AccountAuthenticationForm(request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'User Log in failed.')
        else:
            messages.error(
                request, 'Username or Password Incorrect, User Log in failed.')

    else:
        form = AccountAuthenticationForm()
    context = {"loginform": form}
    return render(request, template_name, context)


@login_required(login_url='account/login')
def logout(request):
    logout(request)
    return redirect('account/login')


# @login_required(login_url='accounts/login')
# def profile_view(request):
#     template_name='accounts/profile.html'
#     args = request.user
#     booking_history = Book.objects.filter(user=args)
#     context={
#         'booking_history':booking_history,
#     }
#     return render(request,template_name,context)

def logout_view(request):
    logoutUser(request)
    return redirect('/')


# def account_view(request):
#     template_name = 'accounts/update.html'
#     if not request.user.is_authenticated:
#         return redirect('login')

#     context = {}

#     if request.POST:
#         form = AccountUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Accout  Updated Successfully.')
#             return redirect('profile')
#         else:
#             messages.error(request, 'Invalid , Not Updated')
#             messages.error(request, form.errors)
#     else:
#         form = AccountUpdateForm(
#             initial={
#                 "email": request.user.email,
#                 "username": request.user.username,
#             }
#         )
#     context['account_form'] = form
#     return render(request, template_name, context)
