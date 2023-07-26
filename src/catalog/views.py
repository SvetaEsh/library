from django.shortcuts import render
from django.views import generic
from . import models
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
class AuthorListView(generic.ListView):
    model=models.Author
    template_name="catalog/list-author.html"
    fields=["first_name", "last_name", "date_of_birth", "date_of_death"]

class AuthorView(generic.DetailView):
    model=models.Author
    template_name="catalog/view-author.html"
    fields=["first_name", "last_name", "date_of_birth", "date_of_death"]

class AuthorDeleteView(PermissionRequiredMixin, generic.DeleteView):
    login_url=reverse_lazy('staff:login')
    model=models.Author
    template_name="catalog/delete-author.html"
    success_url="/"
    permission_required=["catalog.delete_author"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Удалить"
        return context 

class AuthorCreateView(generic.CreateView):
    model=models.Type
    form_class=forms.AuthorModelForm
    template_name="catalog/add-author.html"
    success_url=reverse_lazy("catalog:success-page")
    
def success_page(request):
    return render(request, template_name="catalog/add-succesfully.html", context={"message": f"Создан!"})

class AuthorUpdateView(PermissionRequiredMixin, generic.UpdateView):
    login_url=reverse_lazy('staff:login')
    model=models.Author
    form_class=forms.AuthorModelForm
    template_name="catalog/update-author.html"
    permission_required=["catalog.update_author"]
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

class BookDeleteView(PermissionRequiredMixin, generic.DeleteView):
    login_url=reverse_lazy('staff:login')
    model=models.Book
    template_name="catalog/delete-book.html"
    success_url="/"
    permission_required=["catalog.delete_book"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Удалить"
        return context 

class BookCreateView(generic.CreateView):
    model=models.Book
    form_class=forms.BookModelForm
    template_name="catalog/add-book.html"
    success_url=reverse_lazy("catalog:success-page")
    
class BookUpdateView(PermissionRequiredMixin, generic.UpdateView):
    login_url=reverse_lazy('staff:login')
    model=models.Book
    form_class=forms.BookModelForm
    template_name="catalog/update-book.html"
    permission_required=["catalog.update_book"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить?"
        return context
    