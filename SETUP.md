# Django Ecommerce Project Setup Guide

Complete instructions to set up this Django ecommerce project on a new laptop.

---

## System Requirements

- **Python**: 3.10 or higher (tested with Python 3.13.7)
- **pip**: Package manager (comes with Python)
- **Database**: PostgreSQL (optional - can use SQLite for development)
- **Operating System**: Windows, macOS, or Linux

---

## Step 1: Install Python

Download and install Python from [python.org](https://www.python.org/downloads/)

During installation, **make sure to check** "Add Python to PATH"

Verify installation:
```bash
python --version
pip --version
```

---

## Step 2: Create Virtual Environment

Navigate to your project folder and create a virtual environment:

```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

## Step 3: Install Required Packages

Run this command to install all dependencies:

```bash
pip install django==6.0.1
pip install psycopg2-binary
pip install pillow
pip install google-generativeai
pip install python-decouple
pip install dj-database-url
```

Or use a requirements file (create `requirements.txt` with all packages):

```bash
pip install -r requirements.txt
```

### Complete List of Packages:

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 6.0.1 | Web framework |
| psycopg2-binary | Latest | PostgreSQL adapter |
| pillow | Latest | Image processing (for Product images) |
| google-generativeai | Latest | Gemini AI API integration |
| python-decouple | Latest | Environment variables management |
| dj-database-url | Latest | Parse Railway PostgreSQL connection strings |

---

## Step 4: Database Setup

### Option A: Railway Cloud PostgreSQL (Recommended)

Railway is a cloud platform that hosts PostgreSQL databases. Follow these steps:

1. **Connection String** (Your Railway PostgreSQL URL):
   ```
   postgresql://postgres:ufxHENzWxXrtkrAWmMVxQHeYgcJetHkX@nozomi.proxy.rlwy.net:59873/railway
   ```

2. Update `.env` file with Railway credentials:
   ```bash
   # Railway PostgreSQL Configuration
   DATABASE_URL=postgresql://postgres:ufxHENzWxXrtkrAWmMVxQHeYgcJetHkX@nozomi.proxy.rlwy.net:59873/railway
   ```

3. Update `ecom/settings.py` to use Railway connection:
   ```python
   import dj_database_url
   from decouple import config
   
   # Use Railway PostgreSQL
   DATABASES = {
       'default': dj_database_url.config(
           default=config('DATABASE_URL'),
           conn_max_age=600,
           conn_health_checks=True,
       )
   }
   ```

4. Install dj-database-url package:
   ```bash
   pip install dj-database-url
   ```

**Connection Details Breakdown:**
- **Protocol**: postgresql://
- **Username**: postgres
- **Password**: ufxHENzWxXrtkrAWmMVxQHeYgcJetHkX
- **Host**: nozomi.proxy.rlwy.net
- **Port**: 59873
- **Database**: railway

### Option B: Local PostgreSQL (If you prefer local setup)

1. Install PostgreSQL from [postgresql.org](https://www.postgresql.org/download/)
2. Create a new database:
   ```sql
   CREATE DATABASE ecom_db;
   CREATE USER ecom_user WITH PASSWORD 'your_password';
   ALTER ROLE ecom_user SET client_encoding TO 'utf8';
   ALTER ROLE ecom_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE ecom_user SET default_transaction_deferrable TO on;
   ALTER ROLE ecom_user SET default_transaction_level TO 'read committed';
   GRANT ALL PRIVILEGES ON DATABASE ecom_db TO ecom_user;
   ```

3. Update `ecom/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'ecom_db',
           'USER': 'ecom_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Option C: SQLite (Development/Quick Setup)

SQLite is already configured. No additional setup needed. The database file will be created automatically.

---

## Step 5: Environment Variables

Create a `.env` file in the root directory:

```bash
# .env file

# Railway PostgreSQL Configuration
DATABASE_URL=postgresql://postgres:ufxHENzWxXrtkrAWmMVxQHeYgcJetHkX@nozomi.proxy.rlwy.net:59873/railway

# Gemini API Configuration
GEMINI_API_KEY=AIzaSyAkbdarju5y4TRgDK29gVcXYSfUDeD1efc

# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=127.0.0.1,localhost
```

Update `ecom/settings.py` to use these variables:
```python
import dj_database_url
from decouple import config

# Railway PostgreSQL Database
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Gemini API
GEMINI_API_KEY = config('GEMINI_API_KEY', default='your-api-key')

# Django Config
DEBUG = config('DEBUG', default=True, cast=bool)
SECRET_KEY = config('SECRET_KEY', default='django-insecure-...')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')
```

**Important**: Install the dj-database-url package to parse Railway connection strings:
```bash
pip install dj-database-url
```

---

## Step 6: Run Migrations

Create and apply database migrations:

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

---

## Step 7: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

## Step 8: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

This gathers all CSS, JavaScript, and image files for static content.

---

## Step 9: Run Development Server

```bash
python manage.py runserver 8000
```

Access the application at: **http://127.0.0.1:8000/**

Admin panel: **http://127.0.0.1:8000/admin/**

---

## Project Structure

```
ecom/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database (development)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (create this)
│
├── ecom/                    # Project configuration
│   ├── settings.py          # Main settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   ├── asgi.py              # ASGI configuration
│   └── __pycache__/         # Python cache
│
├── home/                    # Main app (products, cart, checkout)
│   ├── models.py            # Database models
│   ├── views.py             # Business logic
│   ├── urls.py              # App URL routing
│   ├── admin.py             # Admin interface
│   ├── apps.py              # App configuration
│   ├── migrations/          # Database migrations
│   ├── templatetags/        # Custom template filters
│   │   └── home.py          # multiply filter
│   └── tests.py             # Unit tests
│
├── accounts/                # User authentication
│   ├── models.py            # User models
│   ├── views.py             # Authentication logic
│   └── migrations/
│
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   └── home/
│       ├── index.html       # Home page
│       ├── cart.html        # Shopping cart
│       ├── checkout.html    # Checkout process
│       ├── products.html    # Products listing
│       └── ... (other pages)
│
└── static/                  # Static files
    ├── css/
    │   ├── style.css        # Main styles (pure black & white)
    │   ├── override.css     # Bootstrap overrides
    │   └── chatbot.css      # Chatbot widget styles
    └── js/
        └── chatbot.js       # Gemini AI chatbot widget
```

---

## Key Features & Requirements

### AI Chatbot (Gemini API)
- **Package**: google-generativeai
- **API Key**: Required (get from [Google AI Studio](https://aistudio.google.com/app/apikey))
- **Location**: `static/js/chatbot.js` and `home/views.py`

### Image Handling
- **Package**: Pillow
- **Purpose**: Process product images
- **Note**: Products can have optional images (with fallback placeholder)

### Database Models
The project includes:
- **Product**: Store product details (name, price, image, description, rating)
- **Cart**: User shopping carts
- **CartItem**: Items in a cart (with related_name='items')
- **Order**: Customer orders
- **Address**: User delivery addresses

### Custom Django Features
- **Template Filter**: `multiply` filter for price calculations (in `home/templatetags/home.py`)
- **Chatbot**: Floating widget with Gemini AI integration
- **Admin Interface**: Manage products, orders, users through `/admin/`

---

## Important Configuration Files

### `ecom/settings.py`
Main Django configuration - database, installed apps, middleware, templates, static files

### `ecom/urls.py`
Main URL routing configuration

### `home/models.py`
Database models:
```python
- Product (name, price, image, rating, stock)
- Cart (user, timestamp)
- CartItem (cart, product, quantity, with related_name='items')
- Order (user, items, status, total_price)
- Address (user, address, phone)
```

### `home/views.py`
Business logic:
- `home()`: Display featured and latest products
- `view_product()`: Product details page
- `add_to_cart()`: Add items to cart
- `view_cart()`: Display shopping cart
- `checkout()`: Checkout process
- `chatbot_query()`: Handle Gemini AI requests

### `home/templatetags/home.py`
Custom template filter:
- `multiply`: Multiplies two numbers for price calculations

---

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution**: Make sure virtual environment is activated
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Issue: PostgreSQL Connection Error
**Solution**: Check PostgreSQL is running and credentials are correct in `.env`

### Issue: Gemini API errors
**Solution**: Verify API key is correct in `.env` and google-generativeai package is installed

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic --noinput`

### Issue: Database migration errors
**Solution**: 
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Quick Start Checklist

- [ ] Python 3.10+ installed
- [ ] Virtual environment created and activated
- [ ] All packages installed via pip
- [ ] `.env` file created with API keys
- [ ] Database migrations applied (`python manage.py migrate`)
- [ ] Superuser created (`python manage.py createsuperuser`)
- [ ] Static files collected (`python manage.py collectstatic --noinput`)
- [ ] Server running (`python manage.py runserver 8000`)
- [ ] Access http://127.0.0.1:8000/ in browser

---

## Deployment Notes

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Use PostgreSQL instead of SQLite
3. Collect static files: `python manage.py collectstatic --noinput`
4. Use a production WSGI server like Gunicorn
5. Set up proper security headers and HTTPS
6. Keep `.env` file secure (never commit to version control)

---

## Additional Resources

- Django Documentation: https://docs.djangoproject.com/
- Gemini API: https://ai.google.dev/
- PostgreSQL: https://www.postgresql.org/docs/
- Bootstrap 5: https://getbootstrap.com/docs/5.0/

---

**Last Updated**: January 31, 2026  
**Project Version**: 1.0  
**Django Version**: 6.0.1
