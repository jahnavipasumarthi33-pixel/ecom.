# 🧪 Complete Setup & Testing Guide

## Prerequisites Checklist

- [ ] Python 3.8+ installed
- [ ] PostgreSQL 12+ installed and running
- [ ] pip package manager available
- [ ] Text editor or IDE (VS Code recommended)
- [ ] Git (optional)

---

## Step-by-Step Installation

### Phase 1: Environment Setup

#### 1. Open Command Prompt/PowerShell
```bash
# Navigate to project
cd c:\Users\masir\OneDrive\Desktop\Django1\ecom
```

#### 2. Create Virtual Environment
```bash
python -m venv venv
```

#### 3. Activate Virtual Environment
```bash
# Windows PowerShell
venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal line.

#### 4. Upgrade pip
```bash
python -m pip install --upgrade pip
```

---

### Phase 2: Database Setup

#### 1. Create PostgreSQL Database

**Option A: Using pgAdmin (GUI)**
1. Open pgAdmin 4
2. Right-click on Databases
3. Create → Database
4. Name: `cropdb`

**Option B: Using psql (Command Line)**
```sql
psql -U postgres
CREATE DATABASE cropdb;
CREATE USER cropuser WITH PASSWORD 'Janu@2005';
ALTER ROLE cropuser SET client_encoding TO 'utf8';
ALTER ROLE cropuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE cropuser SET default_transaction_deferrable TO on;
ALTER ROLE cropuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE cropdb TO cropuser;
\q
```

#### 2. Test Database Connection
```python
python manage.py dbshell
# Should open PostgreSQL prompt
# Type: \q to exit
```

---

### Phase 3: Dependencies Installation

#### 1. Install Requirements
```bash
pip install -r requirements.txt
```

#### 2. Verify Installations
```bash
pip list
# Should show: Django, psycopg2-binary, Pillow, etc.
```

---

### Phase 4: Django Configuration

#### 1. Run Initial Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

**Output should show:**
```
Operations to perform:
  ...migrations...
Applying admin.0001_initial... OK
Applying auth.0001_initial... OK
... (more migrations)
```

#### 2. Create Superuser Account
```bash
python manage.py createsuperuser
```

**Follow prompts:**
```
Username: admin
Email address: admin@example.com
Password: (enter password)
Password (again): (confirm password)
Superuser created successfully.
```

#### 3. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

**Output should show:**
```
Static files successfully collected...
```

---

### Phase 5: Run Development Server

```bash
python manage.py runserver
```

**Expected output:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

## Testing the Application

### Test 1: Access Homepage
1. Open browser: http://127.0.0.1:8000/
2. Should see:
   - Navigation bar with logo
   - Hero section
   - Featured Products section (empty initially)
   - Footer with links
   - Chatbot in bottom-right corner

### Test 2: Navigation Bar
1. Click "Home" - redirects to home page
2. Click "Products" - shows products page
3. Click "Sign Up" - shows signup page
4. Click "Login" - shows login page

### Test 3: Admin Panel Access
1. Go to: http://127.0.0.1:8000/admin/
2. Log in with superuser credentials
3. Should see Django admin dashboard

### Test 4: Add Sample Data

#### Create a Category
1. In Admin: Click "Categories"
2. Click "Add Category"
3. Fill in:
   - Name: "Electronics"
   - Description: "Electronic gadgets"
4. Click Save

#### Create a Product
1. In Admin: Click "Products"
2. Click "Add Product"
3. Fill in:
   - Name: "Laptop"
   - Category: Select "Electronics"
   - Description: "High-performance laptop"
   - Price: 999.99
   - Discount Price: 799.99
   - Stock: 10
   - Image: Upload a product image
   - Is Featured: Check the box
4. Click Save

#### Add More Products
Repeat the process to add:
- "Smartphone" - $599.99
- "Tablet" - $399.99
- "Headphones" - $149.99

### Test 5: Product Listing
1. Go to: http://127.0.0.1:8000/products/
2. Should see:
   - Product grid (up to 12 products)
   - Category filter sidebar
   - Search box
   - Sort options
   - Pagination

### Test 6: Product Filter
1. Click on "Electronics" in sidebar
2. Products should filter to show only electronics
3. Change sort order - products should reorder

### Test 7: Search Functionality
1. Type "Laptop" in search box
2. Click search button
3. Results should show matching products

### Test 8: Product Detail Page
1. Click on any product
2. Should see:
   - Large product image
   - Product title and description
   - Price and discount
   - Stock status
   - Quantity selector
   - Add to cart button
   - Related products section

### Test 9: Sign Up Process
1. Go to: http://127.0.0.1:8000/signup/
2. Fill in form:
   - Username: testuser
   - Email: test@example.com
   - Password: TestPass123
   - Confirm Password: TestPass123
3. Check "I agree to terms"
4. Click "Create Account"
5. Should redirect to home page
6. Should see success message

### Test 10: Login Process
1. Go to: http://127.0.0.1:8000/login/
2. Fill in:
   - Username: testuser
   - Password: TestPass123
3. Click "Sign In"
4. Should redirect to home page
5. Navbar should show:
   - "Profile" link
   - "Logout" link

### Test 11: Profile Page
1. Click "Profile" in navbar (while logged in)
2. Should see:
   - User information
   - Account statistics
   - Recent orders section
   - Edit profile button

### Test 12: Chatbot Testing
1. Look for chatbot in bottom-right corner
2. Test these conversations:
   - Type "hello" → should respond with greeting
   - Type "products" → should respond about products
   - Type "shipping" → should respond about shipping
   - Type "help" → should respond with help info
   - Type "bye" → should respond with goodbye

### Test 13: Logout
1. Click "Logout" in navbar
2. Should redirect to home page
3. Should see success message
4. Navbar should show "Login" and "Sign Up"

### Test 14: Responsiveness

#### Mobile View (375px)
1. Open DevTools (F12)
2. Click device toggle
3. Select iPhone/Mobile
4. Should see:
   - Hamburger menu
   - Single column layout
   - Touch-friendly buttons
   - Chatbot full width

#### Tablet View (768px)
1. Select iPad/Tablet in DevTools
2. Should see:
   - Responsive grid (2-3 columns)
   - Adjusted navigation
   - Proper spacing

#### Desktop View (1024px+)
1. Full width browser
2. Should see:
   - 4 column product grid
   - Side-by-side layout
   - Full navigation

### Test 15: Error Handling

#### Test 404 Page
1. Go to: http://127.0.0.1:8000/nonexistent/
2. Browser should show 404 or standard error

#### Test Form Validation
1. Go to Sign Up
2. Try submitting empty form
3. Should show validation errors

#### Test Duplicate Login
1. Go to Login
2. Enter wrong password
3. Should show "Invalid username or password!"

---

## Common Issues & Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"
**Solution:**
```bash
pip install -r requirements.txt
# Ensure virtual environment is activated
```

### Issue: Database Connection Error
**Solution:**
1. Verify PostgreSQL is running
2. Check credentials in `ecom/settings.py`
3. Try connection manually:
```bash
python manage.py dbshell
```

### Issue: Static Files Not Loading
**Solution:**
```bash
python manage.py collectstatic --noinput
# Restart server: python manage.py runserver
```

### Issue: Port 8000 Already in Use
**Solution:**
```bash
# Use different port
python manage.py runserver 8001
```

### Issue: Migration Errors
**Solution:**
```bash
# Reset migrations (careful - deletes data)
python manage.py migrate home zero
python manage.py migrate
```

### Issue: Image Upload Not Working
**Solution:**
1. Check `/media/products/` folder exists
2. Verify MEDIA_ROOT in settings.py
3. Restart server

---

## Performance Testing

### Page Load Time
1. Open DevTools → Network tab
2. Reload page
3. Total load time should be < 3 seconds

### Database Queries
1. Enable Django Debug Toolbar (optional)
2. Check number of queries per page
3. Optimize if queries > 10 per request

### Image Optimization
- Recommended image size: < 500KB
- Format: JPG or PNG
- Dimensions: 800x600px minimum

---

## Security Testing

### Test CSRF Protection
1. Add form in template
2. Remove {% csrf_token %}
3. Submit form - should fail

### Test SQL Injection
1. Search for: `' OR '1'='1`
2. Should not break the site
3. Django ORM prevents this

### Test Authentication
1. Try accessing /profile/ without login
2. Should redirect to login page
3. After login, should access

---

## Deployment Checklist

- [ ] DEBUG = False in settings.py
- [ ] ALLOWED_HOSTS configured
- [ ] SECRET_KEY secured
- [ ] Static files collected
- [ ] Database backups set up
- [ ] HTTPS enabled
- [ ] Email configuration tested
- [ ] Error logging configured

---

## Performance Optimization Tips

1. **Enable Caching**
```python
# In settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
```

2. **Database Indexes**
```python
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
```

3. **Query Optimization**
```python
# Use select_related for ForeignKey
products = Product.objects.select_related('category')
```

4. **Image Optimization**
- Use thumbnail packages like Pillow
- Compress images before upload
- Lazy load images

---

## Backup & Recovery

### Backup Database
```bash
# PostgreSQL dump
pg_dump -U cropuser -h localhost cropdb > backup.sql
```

### Restore Database
```bash
psql -U cropuser -h localhost cropdb < backup.sql
```

### Backup Media Files
```bash
# Copy media folder
xcopy media media_backup /E /I
```

---

## Next Steps

After successful testing:

1. ✅ Add more products
2. ✅ Customize colors and branding
3. ✅ Add payment gateway
4. ✅ Set up email notifications
5. ✅ Deploy to production
6. ✅ Monitor performance

---

## Support Resources

- Django Docs: https://docs.djangoproject.com/
- PostgreSQL Docs: https://www.postgresql.org/docs/
- Bootstrap Docs: https://getbootstrap.com/docs/
- Python Docs: https://docs.python.org/

---

**Version**: 1.0
**Last Updated**: January 2024
**Status**: ✅ Production Ready
