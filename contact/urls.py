from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactIndex, name='contactIndex'),
    path('<letter>/', views.contactIndex, name='contactIndex'),
    path('view/<int:id>', views.view, name='contactView'),
    path('edit/<int:id>', views.edit, name='contactEdit'),
    path('create/', views.create, name='contactCreate'),
    path('delete/<int:id>', views.delete, name='contactDelete')
]