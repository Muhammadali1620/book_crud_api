from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListCreateAPIView.as_view()),
    path('<int:pk>/', views.BookRetrieveUpdateDeleteAPIView.as_view()),
]
