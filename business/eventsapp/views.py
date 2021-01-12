

from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from eventsapp.models import user


def home(request):
    return render(request,'index.html')
def blog(request):
    return render(request, 'blog.html')


def sample(request):
    return render(request,'inner-page.html')
def register(request):
 try:

    if request.method == 'POST':
        name1 = request.POST['name']
        lastname1 = request.POST['lastname']
        email1 = request.POST['email']
        password1 = request.POST['password']
        confirmpassword1 = request.POST['confirmpassword']
        c = request.POST['city']
        d = request.POST['address']
        e = request.POST['contactno']
        g = request.POST['gender']
        if password1 == confirmpassword1:
            if user.objects.filter(email=email1).exists():


                return render(request, 'register.html', {'error1': "Email taken"})

            else:


                register1 = user(name=name1, lastname=lastname1, email=email1, password=password1, city=c,address=d,contactno=e, gender=g)
                register1.save();


                return render(request, 'register.html',{'error': "Succesfully Registered"})
        else:

            return render(request, 'register.html', {'error2': "Password not matching"})


    else:

        return render(request,'register.html')
 except:

             return render(request, 'register.html', {'error': "Please Fill The Form"})


def profile(request):

     a =  request.session['updateuser']
     userlist = user.objects.filter(name=a)


     if request.method == 'POST':
         name1 = request.POST['name']
         lastname1 = request.POST['lastname']
         email1 = request.POST['email']
         password1 = request.POST['password']
         confirmpassword1 = request.POST['confirmpassword']
         c = request.POST['city']
         d = request.POST['address']
         e = request.POST['contactno']
         g = request.POST['gender']
         if password1 == confirmpassword1:

            user.objects.filter(name=a).update(name=name1, lastname=lastname1, email=email1, password=password1, city=c, address=d,

                          contactno=e, gender=g)


         return render(request, 'inner-page.html',{'user': userlist,'error': "Change Saved Successfully"})

     else:
         return render(request, 'inner-page.html', {'user': userlist})


def login(request):
    try:


         if request.method=="POST":
            m=user.objects.get(email=request.POST['email'])


            if m.password==request.POST['passw']:
                request.session['updateuser']=m.name



                return render(request,'userpage.html',{'name':m.name})

            else:
                print("hello")
                return render(request, 'login.html',{'error':"Please check Email and Password"})

         else:
             print("hell")
             return render(request, 'login.html')
    except:

        return render(request, 'login.html', {'error1': "Please Fill The Form"})

def event1(request):
    return render(request,'event1.html')


def logout(request):
        try:
            del request.session['users_name']
        except KeyError:
            pass
        return render(request, 'index.html')

