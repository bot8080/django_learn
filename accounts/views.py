from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render


# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']

        # User.object.all()
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Creds')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=email,
                    password=password1,
                    first_name=firstname,
                    last_name=lastname)
                user.save()
                return redirect('login')
                # messages.info(request, 'User created')

        else:
            messages.info(request, 'Password not matched')
            redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def thank_you(request):
    firstname = request.POST['firstname']
    return render(request, 'thank_you.html', {'firstname': firstname})
