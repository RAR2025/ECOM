from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Cart
from django.db.models import Count
from .forms import CustomerRegistrationForm, CustomerProfileForm
from.models import Customer
from django.contrib import messages
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

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user = user, product = product).save()

def show_cart():
    pass