from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from website.models import *
from website.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
import json
import requests

# Create your views here.
def Home(request):
    return render(request,'website/home.html')


def home(request):
    return render(request,'website/home1.html')


def spotlight(request):
    return render(request,'website/spotlight.html')


def photo(request):
    return render(request,'website/dop.html')

def literary(request):
    objects =PublishUser.objects.order_by('-id')
    context = {'lists':objects}
    return render(request,'website/literary.html',context)






def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('website:home',))
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('pass')
            user = authenticate(username= username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('website:home'))
                else:
                    return HttpResponse("Account not active")
            else:
                print("someone tried to login and failed ")
                print(f"Username :{username} and password :{password}")
                return HttpResponse("Invalid login credentials")

        else:
            return render(request,'website/login.html',context={})


# @login_required
# def userinfo(request,pk):
#      model = User.objects.get(id=pk)
#      model1 = model.stories.order_by('-id')
#      print(model)
#      context = {'objects':model1}
#      return render(request,'website/user.html',context)
#


@login_required
def userinfo1(request):
     pk = request.user.id
     model = User.objects.get(id=pk)
     model1 = model.stories.order_by('-id')
     print(model)
     context = {'objects':model1}
     return render(request,'website/user.html',context)


@login_required
def userlogout(request):
        logout(request)
        return HttpResponseRedirect(reverse('website:home'))






def registration(request):
    registered = False
    if request.method == "POST":


        user_form = authenticateform(request.POST)
        mgit_form = MgitForms(request.POST)
        clientkey = request.POST['g-recaptcha-response']
        secretkey = "6LdW1awZAAAAAAywOAedFlMEXxgwhWACCfPaOHDv"
        sdata = {
                'secret':secretkey,
                'response': clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=sdata)
        response = json.loads(r.text)
        verify = response['success']
        print(verify)
        if verify:

            if user_form.is_valid() and  mgit_form.is_valid():
                username = user_form.cleaned_data.get('username')
                password = user_form.cleaned_data.get('password')
                email = user_form.cleaned_data.get('email')
                roll = mgit_form.cleaned_data.get('Roll_number')

                print(username,password)
                user_obj = User(username=username,password= password,email=email)
                mgit_obj = Mgituser(Roll_number=roll)
                mgit_obj.user = user_obj

                user_obj.set_password(user_obj.password)


                user_obj.save()

                mgit_obj.save()


                registered = True

                context={"registered":registered}

                return render(request,'website/signup.html',context)
            else:
                HttpResponse(user_form.errors)
                HttpResponse(mgit_form.errors)

        else:
            HttpResponse('<script> alert("Are you a robot"); </script>')
    else:

        context={"registered":registered}
        return render(request,'website/signup.html',context)



@login_required
def newposter(request):
    if request.method == "POST":
        clientkey = request.POST['g-recaptcha-response']
        secretkey = "6LdW1awZAAAAAAywOAedFlMEXxgwhWACCfPaOHDv"
        sdata = {
                'secret':secretkey,
                'response': clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=sdata)
        response = json.loads(r.text)
        verify = response['success']
        print(verify)
        if verify:
            form = BlogContent1Form(request.POST)
            print('hello1')
            if form.is_valid():
                print('hello2')

                # form.user=user
                # form.save()
                user1= request.user

                user = User.objects.get(id=user1.id)
                # user = request.user.userna
                title = form.cleaned_data['title']
                story = form.cleaned_data['story']


                print('hello3')

                form11 = BlogContent11(user=user,title=title,story=story)

                print('hello4')
                form11.save()
                print('hello5s')
                return HttpResponseRedirect(reverse('website:userinfo'))
            else:
                print(form.errors)
        else:
            HttpResponse('<script> alert("Are you a robot"); </script>')

    else:
        return render(request,'website/newpost.html')






def publish(request,pk):
    content = BlogContent11.objects.get(id=pk)

    print('hello')
    if request.method == "POST":
        print('hello')
        author = request.POST['user']
        title = request.POST['title']
        story = request.POST['story']
        model = PublishUser(author=author,title=title,story=story)
        model.save()
        content = BlogContent11.objects.get(id=pk)
        content.publish = True
        content.save()


        return HttpResponseRedirect(reverse('website:literary'))


def comments(request,pk):
    if request.method == 'POST':
        form = CommentForms( request.POST)
        if form.is_valid():

            content = form.cleaned_data['comment']

            user = PublishUser.objects.get(id=pk)

            model = CommentUser(post=user,comment=content)
            model.save()

            return HttpResponseRedirect(reverse('website:literary'))
        else:
            print(form.errors)
            return HttpResponse("Comment Failed1")

    else:
        return HttpResponse("Comment Failed")
