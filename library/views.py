from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Books, Review
from .forms import ReviewForm, BookForm, LoginForm
from django.contrib.auth import  logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']  
                user_password =  form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'LoggedIn successfully')
                    return HttpResponseRedirect('/book_list/')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/book_list/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



def book_list(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'books': books}) 
def book_detail(request, pk):
    book = Books.objects.get(pk = pk)
    reviews = book.reviews.all()
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})


def add_review(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', pk=book.id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'book': book})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace 'book_list' with your book listing URL name
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})


