from django.shortcuts import render, redirect
from .models import Phone
from django.http import HttpResponse

def index(request):
    return redirect('catalog')


def show_catalog(request):

    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == 'name':
        phone = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phone = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phone = Phone.objects.order_by('-price')
    else:
        phone = Phone.objects.all()


    return render(request, template, {'phones':phone})

    #return HttpResponse(phone[c].slug for c in range(len(phone)))   #узнаем какие есть slug


def show_product(request, slug):
    chosen_phone = Phone.objects.get(slug=slug)      # фильтрация по условию
    template = 'product.html'
    return render(request, template, {'phone':chosen_phone})
