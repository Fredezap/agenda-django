from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def contactIndex(request, letter = None):
    if letter != None:
        contacts = Contact.objects.filter(name__istartswith=letter)
    else:
        name = request.GET.get('search', '').capitalize()
        contacts = Contact.objects.filter(name__contains=name)
    context = {
        'contacts': contacts
    }
    return render(request, '../templates/contact/index.html', context)

def view(request, id):
    # if request.method == "POST":
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }
    return render(request, 'contact/detail.html', context)

def edit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "GET":
        date_created = contact.date
        form = ContactForm(instance = contact)
        context = {
            'form': form,
            'id': id,
            'date_created': date_created,
        }
        return render(request, 'contact/edit.html', context)
    if request.method == "POST":
        form = ContactForm(request.POST, instance = contact)
        contacts = Contact.objects.all()
        context = {
                'id': id,
                'contacts': contacts,
            }
        if form.is_valid():
            form.save()
            messages.success(request, "Contacto actualizado")
            return render(request, 'contact/index.html', context)
        else:
            messages.success(request, "Ocurrio un error")
            return render(request, 'contact/index.html', context)
    
def create(request):
    if request.method == "GET":    
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, 'contact/create.html', context)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contacto creado")
            return redirect('contactIndex')
        else:
            messages.success(request, "Ocurrio un error")
            return redirect('contactIndex')
        
def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contactIndex')