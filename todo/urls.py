from django.urls import path
from . import views

urlpatterns = [
    path('todoIndex/', views.TodoIndex, name='todoIndex'),
    path('view/<int:id>', views.view, name='todoView'),
    path('edit/<int:id>', views.edit, name='todoEdit'),
    path('create/', views.create, name='todoCreate'),
    path('delete/<int:id>', views.delete, name='todoDelete'),
]
