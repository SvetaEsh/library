from django.shortcuts import render
from django.views import generic
from . import models
from . import forms
from django.urls import reverse_lazy

# Create your views here.
class AuthorListView(generic.ListView):
    model=models.Author
    template_name="catalog/list-author.html"
    fields=["first_name", "last_name", "date_of_birth", "date_of_death"]

class AuthorView(generic.DetailView):
    model=models.Author
    template_name="catalog/view-author.html"
    fields=["first_name", "last_name", "date_of_birth", "date_of_death"]

class AuthorDeleteView(generic.DeleteView):
    login_url=reverse_lazy('staff:login')
    model=models.Author
    template_name="catalog/delete-author.html"
    success_url="/"
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Удалить"
        return context 

class AuthorCreateView(generic.CreateView):
    model=models.Author
    form_class=forms.AuthorModelForm
    template_name="catalog/add-author.html"
    success_url=reverse_lazy("catalog:success-page")
    
def success_page(request):
    return render(request, template_name="catalog/add-succesfully.html", context={"message": f"Создан!"})

class AuthorUpdateView(generic.UpdateView):    
    model=models.Author
    form_class=forms.AuthorModelForm
    template_name="catalog/update-author.html"    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить?"
        return context  


class BookListView(generic.ListView):
    model=models.Book
    template_name="catalog/list-book.html"
    form_class=forms.BookModelForm

class BookView(generic.DetailView):
    model=models.Book
    template_name="catalog/view-book.html"
    form_class=forms.BookModelForm

class BookDeleteView(generic.DeleteView):    
    model=models.Book
    template_name="catalog/delete-book.html"
    success_url="/"    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Удалить"
        return context 

class BookCreateView(generic.CreateView):
    model=models.Book
    form_class=forms.BookModelForm
    template_name="catalog/add-book.html"
    success_url=reverse_lazy("catalog:success-page")
    
class BookUpdateView(generic.UpdateView):
    model=models.Book
    form_class=forms.BookModelForm
    template_name="catalog/update-book.html"    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить?"
        return context
    

def home(request):
    books_count=models.Book.objects.all().count()    
    authors_count=models.Author.objects.all().count() 
    return render(
        request,
        'catalog\home.html',
        context={'books':books_count, 'authors':authors_count},
    )