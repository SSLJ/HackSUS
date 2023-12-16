from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
def main(request):
    return render(request, 'main.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            auth_login(request, user)
            return redirect('home')  # Redirect to 'home' URL after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        # Get form data safely using get() method
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if any of the required fields are missing
        if not (username and email and password):
            return render(request, 'signup.html', {'error': 'Please fill in all required fields'})

        # Check if the user already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            # Handle the case where the user already exists
            return render(request, 'signup.html', {'error': 'Username or email already exists'})

        # Create a new user
        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        return redirect('login')

    return render(request, 'signup.html')

def blog(request):
    return render(request, 'blog.html')

def merchandise(request):
    return render(request, 'merchandise.html')

def ecospace(request):
    return render(request, 'ecospace.html')