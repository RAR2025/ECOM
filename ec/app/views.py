from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import Product, Cart
from .forms import CustomerRegistrationForm, CustomerProfileForm
from.models import Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.
def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')



class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category = val).values('title')
        return render(request, "app/category.html",locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html",locals())
    

class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html",locals())
    

class CustomerregistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()    
            messages.success(request,"Congradulation! User register Successfully")
        else:
            messages.warning(request,"Invalid input data")
        return render(request,'app/customerregistration.html',locals())
    



class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Data Input")
        return render(request,'app/profile.html', locals())
    
def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add= Customer.objects.get(pk = pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'app/updateaddress.html',locals())
    def post(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(request.POST, instance=add)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Data Input")
        return redirect('address')


# simple logout wrapper so <a href="{% url 'logout' %}"> works (accepts GET)
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect as _redirect

def logout_view(request):
    """Log out the user and redirect to the login page (accepts GET/POST)."""
    auth_logout(request)
    return _redirect('login')

@login_required
def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1},
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save(update_fields=['quantity'])
    return redirect('showcart')

@login_required
def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    total_cost = sum(item.total_cost for item in cart_items)
    return render(request, 'app/addtocart.html', {
        'cart_items': cart_items,
        'total_cost': total_cost,
    })

@login_required
@require_POST
def update_cart(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk, user=request.user)
    try:
        quantity = int(request.POST.get('quantity', 0))
    except (TypeError, ValueError):
        messages.error(request, 'Enter a valid quantity.')
        return redirect('showcart')

    if quantity < 1:
        cart_item.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'removed': True,
                'cart_count': Cart.objects.filter(user=request.user).count(),
                'cart_total': sum(
                    item.total_cost
                    for item in Cart.objects.filter(user=request.user).select_related('product')
                ),
            })
    else:
        cart_item.quantity = quantity
        cart_item.save(update_fields=['quantity'])
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'removed': False,
                'cart_count': Cart.objects.filter(user=request.user).count(),
                'item_total': cart_item.total_cost,
                'cart_total': sum(
                    item.total_cost
                    for item in Cart.objects.filter(user=request.user).select_related('product')
                ),
            })
    return redirect('showcart')

@login_required
@require_POST
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk, user=request.user)
    cart_item.delete()
    return redirect('showcart')