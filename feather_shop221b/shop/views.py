from django.shortcuts import render, get_object_or_404
from .models import product, Category
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse

#اضافه کردن به سبد خرید 
def add_to_cart(request, product_id):
    product = get_object_or_404(product, id=product_id)
    cart = request.session.get('cart' , {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse('home'))

#نمایش سبد خرید 
def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_price += product_obj.price * quantity
        cart_items.append({'product':product_obj, 'quantity':quantity})
        
    return render(request, 'shop/cart.html',{'cart_items':cart_items , 'total_price':total_price})

#نمایش صفحه اصلی با همه محصولات 
def home(request):
    products = product.objects.all()
    return HttpResponse("<h1>Welcome to Feather Shop 221B!</h1>")
   
#نمایش محصولات یک دسته خاص
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    product = product.objects.filter(category=category)
    return render(request, 'shop/category.html', {'category':category, 'products':products})

# نمایش صفحه جزئیات یک محصول
def product_detail(request, product_id):
    product = get_object_or_404(product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})


