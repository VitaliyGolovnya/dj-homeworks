from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'min_price':
        sort_by = 'price'
    elif sort_by == 'max_price':
        sort_by = '-price'
    template = 'catalog.html'
    phones = Phone.objects.order_by(sort_by)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
