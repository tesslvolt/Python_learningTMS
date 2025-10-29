from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from django.core.mail import EmailMessage
from django.conf import settings

from .forms import RegisterForm, OrderForm
from .models import Product, Category


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # хэшируем пароль
            user.save()
            login(request, user)  # сразу авторизуем пользователя
            return redirect('products')  # редирект на список товаров
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def products_view(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    products = Product.objects.all()
    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_id
    })

def laptops_view(request):
    cat_laptops = Category.objects.mro('Ноутбуки')



@login_required(login_url='/login/')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


@login_required(login_url='/login/')
def add_to_cart(request, product_id):
    """Добавить товар в корзину (через сессию)."""
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
    request.session['cart'] = cart
    return redirect('cart_view')

@login_required(login_url='/login/')
def remove_from_cart(request, product_id):
    """Удалить товар из корзины."""
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
    request.session['cart'] = cart
    return redirect('cart_view')


@login_required(login_url='/login/')
def cart_view(request):
    """Показать корзину."""
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total = sum(p.price for p in products)
    return render(request, 'cart.html', {'products': products, 'total': total})

@login_required(login_url='/login/')
def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            order.user = request.user
            order.save()

            subject = f'Новый заказ от {order.name}'
            body = (
                f'Имя: {order.name}\n'
                f'Email: {order.email}\n'
                f'Телефон: {order.phone}\n'
                f'Адрес: г. {order.city}, ул. {order.street}, д. {order.house}, подъезд: {order.entrance}\n\n'
                f'Сообщение: {order.message}'
            )

            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['твоя_почта@почта.com'],  # сюда будут приходить письма
                headers={'Reply-To': order.email},  # чтобы ответ уходил пользователю
            )
            email_message.send(fail_silently=False)

            return render(request, 'thanks.html', {'name': order.name})
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form})




