from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_obj = list(Phone.objects.all())
    print(type(phones_obj))
    sort_name = request.GET.get('sort')
    print(sort_name)
    if sort_name:
        if sort_name == 'name':
            phones_obj.sort(key=lambda x: x.name)
        if sort_name == 'min_price':
            phones_obj.sort(key=lambda x: x.price)
        if sort_name == 'max_price':
            phones_obj.sort(key=lambda x: x.price, reverse=True)
    context = {'phones': phones_obj}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    print(phone)
    context = {'phone': phone}
    return render(request, template, context)
