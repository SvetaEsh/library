from django.urls import path
from . import views
from rest_framework import routers
from . import apiviews


router = routers.SimpleRouter()
router.register(r'api-author', apiviews.AuthorViewSet)
router.register(r'api-book', apiviews.BookViewSet)
app_name='catalog'

# Standart path urls for view
urlpatterns = [
    path('author/', views.AuthorListView.as_view(), name="author"),
    path('author/<int:pk>', views.AuthorView.as_view(), name="view-author"),
    path('author-delete/<int:pk>', views.AuthorDeleteView.as_view(), name="delete-author"),
    path('author-add/', views.AuthorCreateView.as_view(), name="create-author"),
    path('success-page/', views.success_page, name="success-page"),
    path('author-update/<int:pk>', views.AuthorUpdateView.as_view(), name="update-author"),
    path('book/', views.BookListView.as_view(), name="book"),
    path('book/<int:pk>', views.BookView.as_view(), name="view-book"),
    path('book-delete/<int:pk>', views.BookDeleteView.as_view(), name="delete-book"), 
    path('book-add/', views.BookCreateView.as_view(), name="create-book"),
    path('book-update/<int:pk>', views.BookUpdateView.as_view(), name="update-book")
]

# Only for apiview
urlpatterns += router.urls