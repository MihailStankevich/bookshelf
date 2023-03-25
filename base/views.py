from django.shortcuts import render,redirect
from .models import Book, Author
from django.db.models import Q
from .forms import BookForm, AuthorForm
# Create your views here.

def home(request):
    # all_books = Book.objects.all()
    # authors = Author.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else '' 
    books = Book.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q)
    ) [:3]

    authors = Author.objects.filter(
        Q(name__icontains=q)
    ) [:3]
    context = {'books': books, 'authors': authors}
    return render(request, 'home.html', context)

def author(request, pk):
    author = Author.objects.get(id=pk)
    author_books = author.books.all()
    context = {'author': author, 'author_books': author_books}
    return render(request, 'author.html', context)

def book_form (request):
    params = []
    form = BookForm()
    authors = Author.objects.all()
    if request.method == 'POST':
        # author_name = request.POST.get('author')
        author_names = request.POST.get('author').split(',')
        author_names = [x.strip(' ').lower() for x in author_names]
        for author_name in author_names:
            print(author_name)
            author, created = Author.objects.get_or_create(name=author_name)
            params.append(author) #нельзя было сделать сразу с many to many realtionship value
        b = Book.objects.create(
            # authors=author,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        b.authors.set(params) #поэтому сначала создаем обьект, а потом присваеваем значение
        return redirect('home')
    context = {'form': form, 'authors': authors}
    return render(request, 'book_form.html', context)

def update_author(request, pk):
    author = Author.objects.get(id=pk) #getting author by its pk
    form = AuthorForm(instance=author)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        author.name.lower()
        if form.is_valid():
            form.save()
            return redirect('author', pk=author.id)
    context = {'form':form}
    return render(request, 'update_author.html', context)

def book(request, pk):
    book = Book.objects.get(id=pk)
    context= {'book': book}
    return render(request, 'book.html', context)

def all_books( request ):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'all_books.html', context)

def all_authors( request ):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'all_authors.html', context)


#### доделать отправку формы 