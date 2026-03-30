# Restaurant Delivery Management System - Configuration File

import os

# Flask Configuration
DEBUG = True
SECRET_KEY = 'your_secret_key_here_change_in_production'

# MySQL Configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'restaurant_delivery'
MYSQL_CURSORCLASS = 'DictCursor'

# Application Configuration
APP_HOST = 'localhost'
APP_PORT = 5000
APP_DEBUG = True

# Session Configuration
SESSION_TIMEOUT = 3600  # 1 hour in seconds
PERMANENT_SESSION_LIFETIME = 3600

# Upload Configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Pagination
ITEMS_PER_PAGE = 10

# Email Configuration (for future use)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-password'

# Logging Configuration
LOG_LEVEL = 'INFO'
LOG_FILE = 'app.log'

# Security
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
CORS_ENABLED = False

# API Configuration
API_VERSION = 'v1'
API_TIMEOUT = 30

# Default Settings
DEFAULT_DELIVERY_TIME_LIMIT = 45  # minutes
DEFAULT_CURRENCY = 'INR'

# Delivery Status Options
DELIVERY_STATUS = ['Pending', 'In Transit', 'Delivered', 'Cancelled']
ORDER_STATUS = ['Pending', 'In Transit', 'Delivered', 'Cancelled']
STAFF_STATUS = ['Active', 'Inactive']
