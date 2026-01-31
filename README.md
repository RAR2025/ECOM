# Django E-Commerce Dairy Products Store

A comprehensive Django-based e-commerce web application specifically designed for selling dairy products. This project implements a complete online store with user authentication, product catalog, customer profiles, and administrative features.

## 🎯 Project Overview

This is a full-featured e-commerce platform built with Django 6.0, focusing on dairy products like milk, curd, cheese, ghee, paneer, lassi, milkshakes, and ice cream. The application provides a modern, responsive web interface with Bootstrap 5 styling and includes comprehensive user management, product categorization, and customer profile management.

## 🏗️ Project Architecture

### Core Structure
```
ec/                          # Main Django project directory
├── ec/                      # Project configuration package
│   ├── __init__.py         # Python package marker
│   ├── settings.py         # Django settings configuration
│   ├── urls.py             # Main URL routing configuration
│   ├── wsgi.py             # WSGI application entry point
│   └── asgi.py             # ASGI application entry point
├── app/                     # Main application package
│   ├── migrations/         # Database migration files
│   ├── static/             # Static files (CSS, JS, Images)
│   ├── templates/          # HTML templates
│   ├── __init__.py         # Python package marker
│   ├── admin.py            # Django admin configuration
│   ├── apps.py             # Application configuration
│   ├── forms.py            # Django forms definitions
│   ├── models.py           # Database models
│   ├── tests.py            # Unit tests
│   ├── urls.py             # Application URL patterns
│   └── views.py            # View functions and classes
├── media/                   # User-uploaded files
├── db.sqlite3              # SQLite database file
└── manage.py               # Django management script
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to project directory**
   ```bash
   cd ec
   ```

5. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files (if needed)**
   ```bash
   python manage.py collectstatic
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📦 Dependencies

### Core Dependencies (requirements.txt)
- **django**: Web framework for building the application
- **pillow**: Python Imaging Library for handling product images

### Frontend Dependencies (CDN)
- **Bootstrap 5.3.8**: CSS framework for responsive design
- **jQuery 3.7.1**: JavaScript library for DOM manipulation
- **Font Awesome**: Icon library for UI elements
- **Owl Carousel**: jQuery plugin for image carousels

## 🗄️ Database Schema

### Models Overview

#### Product Model
```python
class Product(models.Model):
    title = models.CharField(max_length=100)           # Product name
    selling_price = models.FloatField()                # Original price
    discounted_price = models.FloatField()             # Sale price
    description = models.TextField()                   # Product description
    composition = models.TextField(default='')        # Product ingredients
    prodapp = models.TextField(default='')             # Product applications
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
```

**Categories Available:**
- CR: CURD
- ML: MILK  
- LS: LASSI
- MS: MILKSHAKE
- PN: PANEER
- GH: GHEE
- CZ: CHEESE
- IC: ICECREAM

#### Customer Model
```python
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Django User
    name = models.CharField(max_length=200)                   # Full name
    locality = models.CharField(max_length=200)               # Area/locality
    city = models.CharField(max_length=50)                    # City
    mobile = models.CharField(max_length=10, validators=[phone_validator], unique=True)
    zipcode = models.IntegerField()                           # Postal code
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
```

**Supported Indian States & Union Territories:**
All 28 states and 8 union territories of India are supported in the dropdown.

### Database Migrations
- **0001_initial.py**: Creates the Product model with all dairy product categories
- **0002_customer.py**: Adds Customer model with user profile information and address details

## 🎨 Frontend Structure

### Templates Directory (`ec/app/templates/app/`)
- **base.html**: Master template with navigation, footer, and common elements
- **home.html**: Homepage with product showcase and banners
- **about.html**: About us page
- **contact.html**: Contact information page
- **category.html**: Product listing by category
- **productdetail.html**: Individual product details page
- **login.html**: User login form
- **customerregistration.html**: New user registration
- **profile.html**: User profile creation/editing
- **address.html**: Customer address management
- **updateaddress.html**: Address editing form
- **changepassword.html**: Password change form
- **passwordchangedone.html**: Password change confirmation

### Static Files (`ec/app/static/app/`)

#### CSS Files
- **style.css**: Custom styles for the application
- **owl.carousel.min.css**: Carousel component styles
- **all.min.css**: Font Awesome icons

#### JavaScript Files
- **myscript.js**: Custom JavaScript functionality
- **owl.carousel.min.js**: Carousel functionality
- **all.min.js**: Font Awesome JavaScript

#### Images
- **banner/**: Homepage banner images (b1.jpg to b4.jpg)
- **product/**: Product images for all dairy items
- **RAR.png**: Company logo

### Media Files (`ec/media/`)
- **product/**: User-uploaded product images
- Handles dynamic image uploads through Django's ImageField

## 🔧 Application Features

### User Authentication System
- **Registration**: New user account creation with email validation
- **Login/Logout**: Secure user authentication
- **Password Management**: Change password functionality
- **Profile Management**: Customer profile creation and editing

### Product Management
- **Category-based Browsing**: Products organized by dairy categories
- **Product Details**: Comprehensive product information display
- **Image Handling**: Product images with upload functionality
- **Search Functionality**: Product search capability (frontend ready)

### Customer Management
- **Profile Creation**: Detailed customer information collection
- **Address Management**: Multiple address support for customers
- **Mobile Validation**: Indian mobile number format validation
- **State Selection**: Dropdown with all Indian states and UTs

### Administrative Features
- **Django Admin**: Full admin interface for managing products and customers
- **Product Admin**: Bulk product management with image preview
- **Customer Admin**: Customer information management

## 🔍 Detailed File Analysis

### Configuration Files

#### `ec/ec/settings.py`
- **Database**: SQLite3 configuration for development
- **Static Files**: Configuration for CSS, JS, and image serving
- **Media Files**: User upload handling setup
- **Security**: Debug mode enabled (development only)
- **Apps**: Includes custom 'app' alongside Django defaults
- **Authentication**: Login redirect to profile page

#### `ec/ec/urls.py`
- **Admin URLs**: Django admin interface routing
- **App URLs**: Includes all application URLs from app.urls
- **Media Serving**: Development media file serving configuration

### Application Logic

#### `ec/app/models.py`
- **Phone Validator**: Custom regex validator for Indian mobile numbers (10 digits starting with 6-9)
- **State Choices**: Complete list of Indian states and union territories
- **Category Choices**: Dairy product categories with short codes
- **Foreign Key Relationships**: Customer linked to Django User model

#### `ec/app/views.py`
- **Function-based Views**: Simple views for static pages (home, about, contact)
- **Class-based Views**: Complex views for product catalog and user management
- **Form Handling**: Registration, profile, and address management
- **Authentication**: Login required for profile operations
- **Message Framework**: Success/error message display

#### `ec/app/forms.py`
- **Custom User Registration**: Extended UserCreationForm with email field
- **Bootstrap Styling**: All forms styled with Bootstrap CSS classes
- **Custom Authentication**: Styled login form
- **Profile Forms**: Customer information collection with validation
- **Password Management**: Custom password change forms

#### `ec/app/admin.py`
- **Product Admin**: Displays all product fields in admin list view
- **Customer Admin**: Shows customer details with user relationship
- **Model Registration**: Both models registered for admin interface

### URL Routing (`ec/app/urls.py`)
- **Homepage**: Root URL routing
- **Product URLs**: Category and detail page routing with parameters
- **Authentication URLs**: Login, registration, password management
- **Profile URLs**: Customer profile and address management
- **Dynamic Routing**: Category and product ID-based URL patterns

## 🔒 Security Features

### Authentication & Authorization
- **CSRF Protection**: Cross-site request forgery protection enabled
- **Password Validation**: Django's built-in password validators
- **Session Management**: Secure session handling
- **Login Required**: Protected views for user-specific operations

### Data Validation
- **Phone Number Validation**: Regex validation for Indian mobile numbers
- **Form Validation**: Server-side form validation for all user inputs
- **Model Constraints**: Database-level constraints and validations

## 🎯 Business Logic

### E-commerce Workflow
1. **Product Browsing**: Users can browse products by category
2. **User Registration**: New customers create accounts
3. **Profile Setup**: Customers add delivery addresses
4. **Product Selection**: Detailed product information display
5. **User Management**: Profile and address management

### Category Management
The application supports 8 main dairy product categories:
- **Milk Products**: Various types of milk (cow, buffalo, toned, etc.)
- **Curd Products**: Different varieties of curd
- **Cheese Products**: Paneer, processed cheese, mozzarella
- **Ghee Products**: Cow and buffalo ghee
- **Beverages**: Lassi and milkshakes
- **Frozen Products**: Ice cream and kulfi

## 🚧 Development Notes

### Current Implementation Status
- ✅ User authentication system
- ✅ Product catalog with categories
- ✅ Customer profile management
- ✅ Admin interface
- ✅ Responsive design
- ⚠️ Shopping cart (frontend ready, backend pending)
- ⚠️ Order management (not implemented)
- ⚠️ Payment integration (not implemented)

### Code Quality Notes
- **Django Best Practices**: Follows Django conventions and patterns
- **Separation of Concerns**: Clear separation between models, views, and templates
- **Reusable Components**: Base template for consistent UI
- **Error Handling**: Form validation and user feedback
- **Responsive Design**: Bootstrap-based mobile-friendly interface

### Database Considerations
- **SQLite**: Suitable for development, consider PostgreSQL for production
- **Image Storage**: Local file storage, consider cloud storage for production
- **Indexing**: Consider adding database indexes for frequently queried fields

## 🔄 Future Enhancements

### Planned Features
1. **Shopping Cart**: Complete cart functionality
2. **Order Management**: Order processing and tracking
3. **Payment Gateway**: Integration with payment providers
4. **Inventory Management**: Stock tracking and management
5. **Email Notifications**: Order confirmations and updates
6. **Search Enhancement**: Advanced product search and filtering
7. **Reviews & Ratings**: Customer product reviews
8. **Wishlist**: Save products for later
9. **Discount System**: Coupon codes and promotional offers

### Technical Improvements
1. **API Development**: REST API for mobile app integration
2. **Caching**: Redis/Memcached for performance
3. **Testing**: Comprehensive unit and integration tests
4. **Deployment**: Production deployment configuration
5. **Monitoring**: Application performance monitoring
6. **Security**: Enhanced security measures for production

## 🐛 Troubleshooting

### Common Issues

1. **Migration Errors**
   ```bash
   python manage.py makemigrations --empty app
   python manage.py migrate --fake-initial
   ```

2. **Static Files Not Loading**
   ```bash
   python manage.py collectstatic --clear
   ```

3. **Image Upload Issues**
   - Ensure media directory has write permissions
   - Check MEDIA_ROOT and MEDIA_URL settings

4. **Database Issues**
   ```bash
   # Reset database
   rm db.sqlite3
   python manage.py migrate
   ```

### Development Tips
- Always activate virtual environment before running commands
- Use Django debug toolbar for development debugging
- Check Django logs for detailed error information
- Ensure all dependencies are installed correctly

## 📝 License & Credits

### Development Information
- **Framework**: Django 6.0
- **Frontend**: Bootstrap 5, jQuery, Font Awesome
- **Database**: SQLite3 (development)
- **Image Processing**: Pillow
- **Developer**: Ruturaj Rajwade (RAR)
- **Year**: 2025

### Made By
**Ruturaj Rajwade**

This comprehensive documentation should help you understand every aspect of the codebase, from installation to deployment, and serve as a complete reference for future development and maintenance.