# Import section.
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create functions.
def user_login(request):
    """
    Display the login page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response with the rendered login page.
    """
    return render(request, 'registration/login.html')


def authenticate_user(request):
    """
    Handle user authentication.

    Args:
        request (HttpRequest): The request object containing the username and password.

    Returns:
        HttpResponseRedirect: Redirects to the login page if authentication fails.
        HttpResponseRedirect: Redirects to the polls index page if authentication is successful.
    """
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
    
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('polls:index'))  # Redirect to polls index page


def show_user(request):
    """
    Display the user page after successful login.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response with the rendered user page, including the username.
    """
    return render(request, 'registration/user.html', {
        "username": request.user.username,
    })


def register(request):
    """
    Handle user registration.

    Args:
        request (HttpRequest): The request object. If the request method is POST, it contains the registration data.

    Returns:
        HttpResponseRedirect: Redirects to the login page after successful registration.
        HttpResponse: The response with the rendered registration page and form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_auth:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Handle user logout
def user_logout(request):
    logout(request)
    return redirect('user_auth:login')