from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm,MyPasswordChangeForm, MySetPasswordForm;
urlpatterns = [
    path("",views.home),
    path('category/<slug:val>',views.CategoryView.as_view(), name="category"),
    path('product-detail/<int:pk>',views.ProductDetail.as_view(), name="product-detail"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('profile/',views.ProfileView.as_view(), name='profile' ),
    path('Address/',views.address, name='address' ),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name ="updateAddress" ),


    #login authentication
    path('registration/',views.CustomerregistrationView.as_view(), name='customerregistration'),
    path('accounts/login',auth_view.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm), name = 'login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url=reverse_lazy('passwordchangedone')), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),  
    path('logout/', views.logout_view, name='logout'),

    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset-done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="app/password-reset-confirm.html", form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name="password_reset_complete"),    
]   
