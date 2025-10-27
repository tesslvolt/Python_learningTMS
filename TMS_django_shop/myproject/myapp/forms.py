from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'in_stock', 'category']


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data


class OrderForm(forms.ModelForm):
    phone = forms.CharField(
        label='Мобильный телефон',
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\+375\d{9}$',
                message="Введите номер телефона в формате +375XXXXXXXXX"
            )
        ]
    )

    class Meta:
        model = Order
        fields = ['name', 'city', 'street', 'house', 'entrance', 'email', 'phone', 'message']

