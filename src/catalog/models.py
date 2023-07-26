from django.db import models

from django.urls import reverse_lazy

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Умер', null = True, blank = True)
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('catalog:view-author', kwargs={"pk": self.pk})

class Book(models.Model):
    name = models.CharField(
        verbose_name = "Название кинги",
        max_length=200
    )
    author = models.ManyToManyField(  
        Author,
        verbose_name="Автор",
        related_name='author_rn'
    )
    description = models.TextField(
        verbose_name = "Описание книги",
        max_length=10000,
        null = True,
        blank = True
    )
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('catalog:view-book', kwargs={"pk": self.pk})
    

