# LinkShort - URL Shortener Web Application

A feature-rich URL shortener web application built with Django, featuring user authentication, analytics, QR code generation, and a modern responsive UI.

## ✨ Features

### Core Requirements ✅

#### 1. **User Authentication**
- ✅ User registration with Django's built-in authentication
- ✅ Secure login/logout functionality
- ✅ Session management
- ✅ Password validation and security
- ✅ Only authenticated users can create and manage URLs

#### 2. **URL Shortening**
- ✅ Convert long URLs into short, shareable links
- ✅ Unique short key generation using custom algorithm
- ✅ Automatic redirection from short URL to original URL
- ✅ Click tracking for each redirect

#### 3. **URL Management**
- ✅ Dashboard to view all created short URLs
- ✅ Edit existing short URLs (change destination, expiration, status)
- ✅ Delete short URLs with confirmation
- ✅ Display creation date and usage statistics
- ✅ Active/Inactive status toggle

#### 4. **Basic Analytics**
- ✅ Click count tracking for each short URL
- ✅ Total clicks across all URLs
- ✅ URLs created today counter
- ✅ Real-time statistics dashboard

#### 5. **User Interface**
- ✅ Clean, modern, and intuitive design
- ✅ Fully responsive layout (mobile, tablet, desktop)
- ✅ Professional color scheme and typography
- ✅ Smooth animations and transitions
- ✅ Icon-based navigation with Font Awesome

### Bonus Features ✅

#### 1. **Custom Short URLs**
- ✅ Users can customize the short code
- ✅ Uniqueness validation
- ✅ Availability checking
- ✅ Minimum length requirements (6-10 characters)

#### 2. **Expiration Time**
- ✅ Optional expiration date/time for short URLs
- ✅ DateTime picker for easy selection
- ✅ Visual indicators for expiring URLs

#### 3. **QR Code Generation**
- ✅ Generate QR codes for any short URL
- ✅ Persistent QR code storage
- ✅ Download QR codes as PNG images
- ✅ Regenerate QR codes on demand


---

## 🛠 Technology Stack

### Backend
- **Django 6.0.2** - Web framework
- **Python 3.12** - Programming language
- **SQLite/PostgreSQL** - Database (SQLite for dev, PostgreSQL for production)
- **Gunicorn** - WSGI HTTP Server

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling with custom design system
- **JavaScript** - Interactive features
- **Font Awesome 6.0** - Icons

### Libraries & Tools
- **qrcode[pil]** - QR code generation
- **Pillow** - Image processing
- **python-decouple** - Environment configuration
- **python-dotenv** - Environment variables
- **dj-database-url** - Database configuration
- **whitenoise** - Static file serving
- **psycopg2-binary** - PostgreSQL adapter

---

## 📁 Project Structure

```
url_shortener/
├── apps/
│   └── shortener/
│       ├── migrations/          # Database migrations
│       ├── __init__.py
│       ├── admin.py            # Admin panel configuration
│       ├── apps.py             # App configuration
│       ├── forms.py            # Form definitions (Create, Edit)
│       ├── models.py           # ShortUrl model
│       ├── services.py         # Business logic (short code generation)
│       ├── qr_service.py       # QR code generation service
│       ├── urls.py             # App URL patterns
│       ├── views.py            # View functions
│       └── tests.py            # Unit tests
├── config/
│   ├── __init__.py
│   ├── asgi.py                 # ASGI configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
├── templates/
│   ├── registration/
│   │   ├── login.html          # Login page
│   │   ├── register.html       # Registration page
│   │   └── logout.html         # Logout confirmation
│   ├── shortener/
│   │   ├── dashboard.html      # Main dashboard
│   │   ├── create.html         # Create short URL form
│   │   ├── create_success.html # Success page
│   │   ├── edit_url.html       # Edit URL form
│   │   ├── confirm_delete.html # Delete confirmation
│   │   └── qr_code_view.html   # QR code display
│   ├── base.html               # Base template
│   └── 404.html                # Custom 404 page
├── media/
│   └── qr_codes/               # Generated QR code images
├── staticfiles/                # Collected static files
├── venv/                       # Virtual environment
├── .env                        # Environment variables (not in repo)
├── .gitignore                  # Git ignore rules
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git
- Virtual environment tool (venv)

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd url_shortener
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### Step 5: Database Setup

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser
```

### Step 6: Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📖 Usage Guide

### 1. User Registration

1. Navigate to the registration page
2. Enter username, email (optional), and password
3. Confirm password
4. Click "Create Account"

### 2. Creating Short URLs

1. Log in to your account
2. Click "Create Short URL" from dashboard
3. Enter the long URL you want to shorten
4. **Optional**: Check "Custom short code" to create a custom URL
5. **Optional**: Check "Set expiration time" to add an expiration date
6. Click "Create Short URL"
7. Copy your shortened URL or generate a QR code

### 3. Managing URLs

**View Dashboard:**
- See all your created short URLs
- View statistics (clicks, creation date, expiration)
- Check active/inactive status

**Edit URL:**
- Click "Edit" button on any URL
- Modify destination URL, expiration, or active status
- Save changes

**Delete URL:**
- Click "Delete" button
- Confirm deletion
- URL and associated QR code are permanently removed

### 4. QR Code Features

**Generate QR Code:**
- Click "Generate QR" on any URL without a QR code
- QR code is created and saved

**View QR Code:**
- Click "View QR" to see the QR code
- View URL details and statistics

**Download QR Code:**
- Click "Download QR Code" button
- PNG image is downloaded to your device

**Regenerate QR Code:**
- Click "Regenerate QR" to create a new QR code
- Old QR code is replaced

---

## 🔧 Core Features Implementation

### 1. User Authentication System

**Implementation Details:**
- Uses Django's built-in authentication framework
- Custom registration view with `UserCreationForm`
- Login/logout views with session management
- `@login_required` decorator protects all URL management views
- Password validation with Django's validators

**Files:**
- `apps/shortener/views.py` - `signup()`, login/logout views
- `templates/registration/` - Authentication templates

### 2. URL Shortening Algorithm

**Short Code Generation:**
```python
def generate_unique_short_code(length=6):
    """
    Generates a unique short code using alphanumeric characters
    - Uses random.choices with string.ascii_letters + string.digits
    - Ensures uniqueness by checking database
    - Default length: 6 characters
    - Character set: a-z, A-Z, 0-9 (62 possible characters)
    """
```

**Features:**
- Base62-like encoding (alphanumeric)
- Collision detection and retry mechanism
- Configurable length (default 6 characters)
- ~56 billion possible combinations with 6 characters

**Files:**
- `apps/shortener/services.py` - `generate_unique_short_code()`

### 3. URL Redirection

**Implementation:**
```python
def redirect_short_url(request, short_code):
    """
    1. Lookup short URL by code
    2. Check if active and not expired
    3. Increment click count
    4. Redirect to original URL
    5. Return 404 if not found
    """
```

**Features:**
- Atomic click count increment
- Expiration checking
- Active status validation
- Custom 404 page for broken links

**Files:**
- `apps/shortener/views.py` - `redirect_short_url()`

### 4. Analytics System

**Tracked Metrics:**
- Individual URL click counts
- Total clicks across all URLs
- URLs created today
- Creation timestamps
- Last modified timestamps

**Dashboard Statistics:**
- Real-time data using Django ORM aggregation
- Efficient database queries with `Sum()` and `Count()`
- Visual stat cards with icons

**Files:**
- `apps/shortener/views.py` - `dashboard()` view
- `templates/shortener/dashboard.html` - Statistics display

### 5. Responsive UI Design

**Design System:**
- CSS custom properties for theming
- Mobile-first responsive approach
- Breakpoints: 768px (tablet), 480px (mobile)
- Flexbox and Grid layouts
- Smooth transitions and animations

**Color Palette:**
- Primary: `#4f46e5` (Indigo)
- Success: `#10b981` (Green)
- Danger: `#ef4444` (Red)
- Warning: `#f59e0b` (Amber)

**Files:**
- `templates/base.html` - Base template with design system
- All template files - Responsive components

---

## 🎁 Bonus Features Implementation

### 1. Custom Short URLs

**Implementation:**
- Checkbox to enable custom code input
- JavaScript toggle for conditional field display
- Server-side validation for uniqueness
- Length validation (6-10 characters)
- Alphanumeric character restriction

**Validation:**
```python
def clean_custom_short_code(self):
    """
    - Checks if custom code is provided when checkbox is checked
    - Validates uniqueness against database
    - Returns None if checkbox unchecked
    """
```

**Files:**
- `apps/shortener/forms.py` - `ShortUrlForm` with custom validation
- `templates/shortener/create.html` - Conditional field display

### 2. Expiration Time

**Implementation:**
- Optional datetime field with HTML5 datetime-local input
- Checkbox to enable expiration
- Future date validation
- Automatic expiration handling on redirect
- Visual badges for expiring URLs

**Features:**
- User-friendly datetime picker
- Timezone-aware datetime handling
- "Never expires" option (default)
- Expiration date display in dashboard

**Files:**
- `apps/shortener/forms.py` - Expiration validation
- `apps/shortener/models.py` - `expires_at` field
- `templates/shortener/create.html` - Datetime input

### 3. QR Code Generation

**Implementation:**
```python
def generate_qr_code(short_url_instance, request):
    """
    1. Build full short URL
    2. Create QR code with qrcode library
    3. Save as PNG image
    4. Store in media/qr_codes/
    5. Update database with image path and timestamp
    """
```

**Features:**
- On-demand QR generation (not automatic)
- Persistent storage in database
- PNG format with configurable size
- Error correction level L (7% recovery)
- Download functionality
- Regeneration capability
- Automatic cleanup on URL deletion

**QR Code Specifications:**
- Format: PNG
- Size: 10 pixels per box
- Border: 4 boxes
- Error correction: Level L
- Colors: Black on white

**Files:**
- `apps/shortener/qr_service.py` - QR generation logic
- `apps/shortener/views.py` - QR-related views
- `templates/shortener/qr_code_view.html` - QR display page

---

## 🔗 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET/POST | `/signup/` | User registration | No |
| GET/POST | `/login/` | User login | No |
| POST | `/logout/` | User logout | Yes |

### URL Management
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/dashboard/` | View all URLs | Yes |
| GET/POST | `/create/` | Create short URL | Yes |
| GET/POST | `/urls/<id>/edit/` | Edit URL | Yes |
| GET/POST | `/delete/<id>` | Delete URL | Yes |
| GET | `/<short_code>/` | Redirect to original URL | No |

### QR Code Operations
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/qr/<id>/generate/` | Generate QR code | Yes |
| GET | `/qr/<id>/view/` | View QR code | Yes |
| GET | `/qr/<id>/download/` | Download QR code | Yes |
| GET | `/qr/<id>/regenerate/` | Regenerate QR code | Yes |

---

## 🗄 Database Schema

### ShortUrl Model

```python
class ShortUrl(models.Model):
    user = ForeignKey(User)              # Owner of the URL
    original_url = URLField()            # Long URL to redirect to
    short_code = CharField(max_length=10) # Unique short identifier
    click_count = PositiveIntegerField()  # Number of clicks
    created_at = DateTimeField()         # Creation timestamp
    expires_at = DateTimeField(null=True) # Optional expiration
    is_active = BooleanField()           # Active/Inactive status
    qr_code_image = ImageField(null=True) # QR code image file
    qr_code_generated_at = DateTimeField(null=True) # QR generation time
```

**Relationships:**
- Many-to-One with User (one user can have many URLs)

**Indexes:**
- `short_code` - For fast lookup during redirects
- `user` - For efficient user-specific queries

---

## 🚀 Deployment

### Production Setup (Railway/Heroku)

1. **Environment Variables:**
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:pass@host:port/dbname
ALLOWED_HOSTS=your-domain.com
```

2. **Static Files:**
```bash
python manage.py collectstatic --noinput
```

3. **Database Migration:**
```bash
python manage.py migrate
```

4. **Run with Gunicorn:**
```bash
gunicorn config.wsgi:application
```

### Railway Deployment

The application is configured for Railway deployment:
- `Procfile` for process management
- `runtime.txt` for Python version
- PostgreSQL database integration
- Automatic static file serving with WhiteNoise

**Live Demo:** [https://urlshortener-production-4598.up.railway.app](https://urlshortener-production-4598.up.railway.app)
