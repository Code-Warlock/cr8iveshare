from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Account, Profile
from core.models import FollowersCount, Post
import random
from itertools import chain
# from .models import Profile
# Create your views here.


def index(request):
    # user_object = Account.objects.get(username=request.user.username)
    # print(user_object)
    # user_profile = Profile.objects.get(user=user_object)
    user_following_list = []
    feed = []
    user_following = FollowersCount.objects.filter(
        followers=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)

    # content creator suggestion
    all_users = Account.objects.all()
    user_following_all = []

    new_suggestions_list = [x for x in list(
        all_users) if (x not in list(user_following_all))]
    current_user = Account.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(
        new_suggestions_list) if (x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    feed = Post.objects.all()
    context = {
        # 'user_profile': user_profile,
        'posts': feed,
        'suggestions_username_profile_list': suggestions_username_profile_list[:8],
    }

    template_name = "index.html"
    return render(request, template_name, context)


def about(request):
    template_name = "about.html"
    return render(request, template_name)


def contact(request):
    template_name = "contact.html"
    return render(request, template_name)


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, "Email already exists")
#                 return redirect('signup')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request, "Username already exists")
#                 return redirect('signup')
#             else:
#                 user = User.objects.create_user(
#                     username=username, email=email, password=password)
#                 user.save()

#                 # log in user and redirect to settings page
#                 user_login = auth.authenticate(
#                     username=username, password=password)
#                 auth.login(request, user_login)

#                 # create a profile object for the new user
#                 user_model = User.objects.get(username=username)
#                 # new_profile = Profile.objects.create(
#                 #     user=user_model, id_user=user_model.id)
#                 # new_profile.save()
#                 return redirect('settings')
#         else:
#             messages.info(request, 'Password mismatch')
#             return redirect('signup')
#     else:
#         return render(request, 'signup.html')


# def signin(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, 'Credentials invalid')
#             return redirect('signin')
#     else:
#         return render(request, 'login/index.html')


# @login_required(login_url='signin')
# def logout(request):
#     auth.logout(request)
#     return redirect('signin')
