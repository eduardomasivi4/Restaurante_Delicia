from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import MenuItem
from .forms import ReservaForm

def home(request):
    menu_items = MenuItem.objects.all()

    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReservaForm()

    context = {
        'menu_items': menu_items,
        'form': form
    }

    return render(request, 'restaurante/index.html', context)