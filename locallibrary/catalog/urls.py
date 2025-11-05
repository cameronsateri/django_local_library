# (LAB03)
from django.urls import path
from . import views

urlpatterns = [

]

# (LAB07)
urlpatterns = [
    path('', views.index, name='index'),
]

# (LAB08)
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

# (LAB10)
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]