from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordRestForm
urlpatterns = [
    path("",views.home),
    path('category/<slug:val>',views.CategoryView.as_view(), name="category"),
    path('product-detail/<int:pk>',views.ProductDetail.as_view(), name="product-detail"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('profile/',views.ProfileView.as_view(), name='profile' ),
    path('Address/',views.ProfileView.as_view(), name='address' ),


    #login authentication
    path('registration/',views.CustomerregistrationView.as_view(), name='customerregistration'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class = MyPasswordRestForm),name='password_reset'),
    path('accounts/login',auth_view.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm), name = 'login'),
    
]   
