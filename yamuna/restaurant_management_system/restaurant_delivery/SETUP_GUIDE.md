# Restaurant Delivery Management System - Setup Guide

Complete step-by-step guide to set up the Restaurant Delivery Management System on your machine.

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
2. **MySQL Server** - [Download MySQL](https://dev.mysql.com/downloads/mysql/)
3. **MySQL Workbench** (Optional) - [Download MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
4. **Git** (Optional) - [Download Git](https://git-scm.com/download/win)

## Installation Steps

### Step 1: Install Python

1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. **IMPORTANT**: Check "Add Python to PATH"
4. Click "Install Now"
5. Close the installer

**Verify Installation**:
```bash
python --version
pip --version
```

### Step 2: Install MySQL Server

1. Download MySQL Server from https://dev.mysql.com/downloads/mysql/
2. Run the installer (MSI installer recommended)
3. Follow the installation wizard
4. Choose "Development Default" setup type
5. Keep default settings (Port: 3306)
6. Configure MySQL Server as a Windows Service
7. Set root password (remember this!)
8. Complete installation

**Verify Installation**:
Open Command Prompt and run:
```bash
mysql --version
```

### Step 3: Clone or Download Project

**Option A: Download ZIP**
1. Download the project as ZIP
2. Extract to desired location (e.g., `C:\Users\YourUsername\Desktop\restaurant_delivery`)

**Option B: Using Git**
```bash
git clone <repository-url>
cd restaurant_delivery
```

### Step 4: Setup Python Virtual Environment

Navigate to project directory:
```bash
cd C:\Users\YourUsername\Desktop\restaurant_delivery
```

Create virtual environment:
```bash
python -m venv venv
```

Activate virtual environment:
```bash
# On Windows:
venv\Scripts\activate

# You should see (venv) before your command prompt
```

### Step 5: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask 2.3.2
- Flask-MySQLdb 1.0.1
- MySQLdb 1.2.5
- Werkzeug 2.3.6

### Step 6: Create MySQL Database

**Option A: Using MySQL Command Line**

Open Command Prompt (or PowerShell) and connect to MySQL:
```bash
mysql -u root -p
```

Enter your MySQL root password when prompted.

Then paste this command to create the database:
```sql
source C:/Users/YourUsername/Desktop/restaurant_delivery/database/restaurant_delivery.sql
```

Or copy and paste the entire content of `restaurant_delivery.sql` directly.

**Option B: Using MySQL Workbench**

1. Open MySQL Workbench
2. Connect to your MySQL server
3. File → Open SQL Script
4. Select `database/restaurant_delivery.sql`
5. Click the lightning bolt (Execute) icon
6. Confirm the database is created

**Verify Database Creation**:
```sql
SHOW DATABASES;
```

You should see `restaurant_delivery` in the list.

### Step 7: Configure Database Connection

Open `app.py` file and update these lines (around line 14-18):

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'           # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'your_password'  # Your MySQL password
app.config['MYSQL_DB'] = 'restaurant_delivery'
```

Change the password to your MySQL root password.

### Step 8: Run the Application

Make sure virtual environment is activated (you should see `(venv)` in command prompt):

```bash
python app.py
```

You should see output like:
```
WARNING in app.run_simple - Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 9: Access the Application

1. Open your web browser
2. Go to: http://localhost:5000
3. You should see the home page of Restaurant Delivery Management System

## Troubleshooting

### Issue: Python not found
**Solution**:
1. Ensure Python is added to PATH
2. Restart Command Prompt/PowerShell after installation
3. Use `python` or `python3` (try both)

### Issue: MySQLdb installation fails
**Solution**:
```bash
pip install --upgrade setuptools
pip install -r requirements.txt
```

### Issue: MySQL connection error
**Error**: "No such file or directory: 'localhost' or 'root'"

**Solution**:
1. Ensure MySQL Server is running
2. Check username and password in app.py
3. Try connecting manually:
   ```bash
   mysql -u root -p
   ```
4. Verify credentials

### Issue: Database not found
**Solution**:
1. Verify database creation:
   ```sql
   SHOW DATABASES;
   ```
2. If not present, run the SQL script again
3. Check for errors in the script execution

### Issue: Port 5000 already in use
**Solution**: Change port in app.py (line ~274):
```python
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)  # Changed from 5000 to 5001
```

### Issue: Permission denied errors
**Solution**:
1. Run Command Prompt as Administrator
2. Delete `venv` folder and recreate virtual environment
3. Reinstall dependencies

### Issue: Flask import error
**Solution**:
```bash
# Ensure virtual environment is activated
venv\Scripts\activate

# Reinstall Flask
pip uninstall Flask
pip install Flask==2.3.2
```

## Development Workflow

### Start Development Session

1. Open Command Prompt
2. Navigate to project directory:
   ```bash
   cd C:\Users\YourUsername\Desktop\restaurant_delivery
   ```
3. Activate virtual environment:
   ```bash
   venv\Scripts\activate
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Access at http://localhost:5000

### Deactivate Virtual Environment

```bash
deactivate
```

## Database Management

### View Tables
```sql
USE restaurant_delivery;
SHOW TABLES;
```

### View Customers
```sql
SELECT * FROM Customers;
```

### View Orders
```sql
SELECT * FROM Orders;
```

### Reset Database (Delete all data)
```sql
USE restaurant_delivery;
DROP DATABASE restaurant_delivery;
```

Then re-run the SQL script to create fresh database.

## File Structure Explanation

```
restaurant_delivery/
├── app.py                      # Main Flask application
├── app.py.bak                  # Backup of app.py
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── SETUP_GUIDE.md             # This file
├── .gitignore                 # Git ignore rules
│
├── database/
│   └── restaurant_delivery.sql # SQL database schema
│
├── templates/                  # HTML templates directory
│   ├── index.html             # Home page
│   ├── dashboard.html         # Dashboard
│   ├── customers.html         # Customers page
│   ├── orders.html            # Orders page
│   ├── staff.html             # Staff page
│   ├── deliveries.html        # Deliveries page
│   ├── customer_orders.html   # Customer orders
│   ├── daily_report.html      # Daily report
│   ├── staff_performance.html # Staff performance
│   └── delayed_orders.html    # Delayed orders
│
└── static/                     # Static files directory
    ├── css/
    │   └── style.css          # Stylesheet
    └── js/
        └── script.js          # JavaScript
```

## First Time Usage

1. **Add Customers**: Go to Customers page and add at least one customer
2. **Create Orders**: Go to Orders page and create orders for customers
3. **Manage Staff**: Add delivery staff members on Staff page
4. **Assign Deliveries**: On Deliveries page, assign pending orders to staff
5. **Update Status**: Update delivery status and add customer feedback
6. **View Reports**: Check Reports for analytics

## Next Steps

1. Change the Flask secret key in app.py for security
2. Explore the sample data in the database
3. Review SQL procedures and functions
4. Customize the application for your needs
5. Deploy to a web server (Heroku, AWS, etc.)

## Additional Resources

- Flask Documentation: https://flask.palletsprojects.com/
- MySQL Documentation: https://dev.mysql.com/doc/
- Python Virtual Environments: https://docs.python.org/3/tutorial/venv.html
- SQLite vs MySQL: https://www.mysql.com/

## Support

If you encounter issues:
1. Check the Troubleshooting section above
2. Review the README.md file
3. Check error messages carefully
4. Ensure all prerequisites are installed
5. Verify MySQL is running

## Security Notes for Production

⚠️ **Important**: Before deploying to production:

1. Change `SECRET_KEY` in app.py
2. Set `DEBUG = False`
3. Use environment variables for database credentials
4. Implement user authentication
5. Use HTTPS/SSL
6. Add input validation
7. Implement proper error handling
8. Use a production WSGI server (Gunicorn, uWSGI)
9. Set up database backups
10. Implement logging and monitoring

---

**Happy developing! 🚀**

For questions or issues, please refer to the README.md or Flask documentation.
