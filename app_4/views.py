from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import ProdFormWidget, ProdChoiceForm
from .models import Product
from logging import getLogger

logger = getLogger(__name__)


def index(request):
    return render(request, 'app_4/index.html')


def upd_prod_form(request, product_id):
    if request.method == 'POST':
        form = ProdFormWidget(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            description = form.cleaned_data.get('description')
            number = form.cleaned_data.get('number')
            logger.info(f'Получили {form.cleaned_data=}.')

            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

            product = Product.objects.filter(pk=product_id).first()
            product.name = name
            product.price = price
            product.description = description
            product.quantity = number
            product.image = image.name
            product.save()
            return redirect(request.path)
    else:
        form = ProdFormWidget()
    return render(request, 'app_4/upd_prod.html', {'form': form})


def upd_prod_id_form(request):
    if request.method == 'POST':
        form = ProdChoiceForm(request.POST)
        if form.is_valid():
            prod_id = form.cleaned_data.get('product_id')
            logger.info(f'Получили {form.cleaned_data=}.')
            return redirect(f'/product_update/{prod_id}')
    else:
        form = ProdChoiceForm()
    return render(request, 'app_4/upd_prod_id.html', {'form': form})
