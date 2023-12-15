from django import forms
from app_4.models import Product


class ProdFormWidget(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': f'Введите название товара:'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    number = forms.IntegerField(min_value=0)
    image = forms.ImageField()


class ProdChoiceForm(forms.Form):
    products = Product.objects.all()
    product_id = forms.ChoiceField(label='Product', choices=[(product.id, product.name) for product in products])


class ImageForm(forms.Form):
    image = forms.ImageField()
