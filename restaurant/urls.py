from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.bookingView.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]