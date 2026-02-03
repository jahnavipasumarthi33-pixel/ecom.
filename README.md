# EStore - Modern Django Ecommerce Website

A fully functional ecommerce website built with Django with modern features including user authentication, product catalog, shopping cart, and interactive chatbot.

## Features

✨ **User Management**
- Sign up and login functionality
- User profile management
- Order history tracking
- Wishlist support

🛍️ **Product Management**
- Beautiful product catalog with filtering
- Product search functionality
- Advanced sorting options
- Product details page with ratings
- Category-based navigation
- Stock management
- Discount pricing

💬 **Interactive Chatbot**
- AI-powered customer support chatbot
- Responsive design
- Available on all pages
- Smart keyword-based responses
- Mobile optimized

📱 **Responsive Design**
- Fully responsive across all devices
- Mobile-friendly navigation
- Adaptive layout for tablets and smartphones
- Touch-friendly interface

🎨 **Modern UI/UX**
- Beautiful gradient design
- Smooth animations and transitions
- Professional card layouts
- Intuitive user interface
- Bootstrap 5 framework

🔒 **Security**
- CSRF protection
- Secure password hashing
- Database security with PostgreSQL
- Form validation

📊 **Admin Panel**
- Complete product management
- Order management
- Category management
- User management
- Advanced filtering and search

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

### Step 1: Clone or Download the Project
```bash
cd c:\Users\masir\OneDrive\Desktop\Django1\ecom
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Database
Make sure PostgreSQL is running with the following credentials:
- Database: `cropdb`
- User: `cropuser`
- Password: `Janu@2005`
- Host: `localhost`
- Port: `5432`

Or create the database and user:
```sql
CREATE DATABASE cropdb;
CREATE USER cropuser WITH PASSWORD 'Janu@2005';
ALTER ROLE cropuser SET client_encoding TO 'utf8';
ALTER ROLE cropuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE cropuser SET default_transaction_deferrable TO on;
ALTER ROLE cropuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE cropdb TO cropuser;
```

### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### Step 7: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 8: Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
ecom/
├── accounts/              # User authentication app
│   ├── views.py          # Login, signup, profile views
│   ├── models.py         # User-related models
│   └── admin.py          # Admin configuration
│
├── home/                  # Main app
│   ├── views.py          # Home, products, details views
│   ├── models.py         # Product, Category, Order models
│   └── admin.py          # Admin panel configuration
│
├── templates/             # HTML templates
│   ├── base.html         # Base template with navbar and footer
│   ├── accounts/         # Authentication templates
│   └── home/             # Product templates
│
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Custom styling
│   └── js/
│       └── chatbot.js    # Chatbot functionality
│
├── media/                # User-uploaded files
│   └── products/         # Product images
│
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Usage

### Admin Panel
1. Navigate to `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Add products, categories, manage orders, etc.

### Create Products
1. Go to Admin Panel
2. Click on "Products"
3. Click "Add Product"
4. Fill in product details:
   - Name
   - Category
   - Description
   - Price
   - Discount Price (optional)
   - Stock
   - Image
   - Mark as Featured (optional)

### Manage Categories
1. Go to Admin Panel
2. Click on "Categories"
3. Create new categories for organizing products

## Pages

📄 **Home Page**
- Featured products showcase
- Latest products section
- Category highlights
- Call-to-action buttons

🛒 **Products Page**
- Complete product catalog
- Advanced filtering by category
- Search functionality
- Sorting options (newest, price, name)
- Pagination
- Stock status display

📋 **Product Detail Page**
- High-quality product image
- Detailed description
- Price and discount information
- Stock availability
- Related products
- Product ratings and reviews
- Social sharing options

👤 **User Pages**
- Sign Up page with validation
- Login page with remember me
- User Profile page
- Order history
- Account statistics

## Chatbot Features

The interactive chatbot supports queries about:
- General greetings
- Product information
- Shipping details
- Return policy
- Pricing
- Account creation
- Payment methods
- Discounts
- And more!

The chatbot learns from keywords and provides relevant responses. You can customize responses in `static/js/chatbot.js`.

## Customization

### Change Brand Colors
Edit `static/css/style.css` and modify the CSS variables:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    /* ... other colors ... */
}
```

### Modify Product Fields
Edit `home/models.py` and add new fields to the `Product` model:
```python
class Product(models.Model):
    # Existing fields...
    new_field = models.CharField(max_length=100)  # Add new field
```

Then run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Customize Chatbot Responses
Edit `static/js/chatbot.js` and add/modify bot responses in the `botResponses` object:
```javascript
const botResponses = {
    'your-keyword': 'Your response here',
    // ... more responses ...
};
```

## Database Models

### Product
- Name, Description, Price
- Category (ForeignKey)
- Discount Price, Stock
- Image and Rating
- Created/Updated timestamps
- Featured flag

### Category
- Name, Description
- Created timestamp

### Cart & CartItem
- User cart management
- Product quantities
- Timestamps

### Order & OrderItem
- Order creation and tracking
- Order status (pending, confirmed, shipped, delivered, cancelled)
- Shipping address and details
- Order items and pricing

## Security Considerations

✅ CSRF Protection enabled
✅ SQL Injection prevention through ORM
✅ Secure password storage with hashing
✅ Database connection security
✅ Input validation on forms
✅ User authentication decorators

## Performance Optimization

⚡ Database query optimization with select_related
⚡ Pagination for large product lists
⚡ CSS and JS minification
⚡ Image optimization recommendations
⚡ Caching headers for static files

## Troubleshooting

### Database Connection Error
- Ensure PostgreSQL is running
- Verify credentials in `ecom/settings.py`
- Check PostgreSQL is accessible on localhost:5432

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Migration Issues
```bash
python manage.py migrate --fake-initial
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Future Enhancements

🚀 Add payment gateway integration (Stripe, PayPal)
🚀 Email notifications for orders
🚀 Advanced analytics and reporting
🚀 Multi-language support
🚀 Product reviews and ratings system
🚀 Wishlist functionality
🚀 Recommendation engine
🚀 Admin dashboard analytics
🚀 Inventory management system
🚀 SEO optimization

## Support

For issues or questions, please create an issue in the project repository.

## License

This project is open-source and available under the MIT License.

---

**Happy Shopping! 🛍️**

Built with ❤️ using Django and Bootstrap
