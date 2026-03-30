# Restaurant Delivery Management System - FAQ & Troubleshooting

Common questions and solutions for the Restaurant Delivery Management System.

---

## ❓ Frequently Asked Questions (FAQ)

### General Questions

**Q1: What is the Restaurant Delivery Management System?**
A: It's a complete web-based application for managing restaurant deliveries, including customer management, order tracking, delivery assignment, and performance analytics.

**Q2: What are the system requirements?**
A: 
- Python 3.7 or higher
- MySQL Server 5.7 or higher
- 256MB RAM minimum
- 500MB disk space
- Windows, Linux, or Mac OS
- Modern web browser

**Q3: How long does setup take?**
A: Typically 10-15 minutes if all prerequisites are installed.

**Q4: Is there a mobile version?**
A: Currently, only web version. Mobile-responsive design included. Native mobile app planned for Phase 2.

**Q5: Can I customize the system?**
A: Yes! All code is open, modular, and well-documented. Easy to customize.

**Q6: Is authentication included?**
A: No, basic version is without authentication. Can be added as an enhancement.

**Q7: What's the default admin credentials?**
A: No credentials needed in default version. Just access http://localhost:5000

**Q8: Can I use SQLite instead of MySQL?**
A: Not in current version, but could be modified. MySQL is recommended.

---

### Installation & Setup

**Q9: Python command not found**
A: Python is not in your system PATH. 
- Reinstall Python and check "Add Python to PATH"
- Or add Python to PATH manually
- Restart command prompt after installation

**Q10: How do I check if MySQL is installed?**
A: Run in command prompt:
```bash
mysql --version
```

**Q11: MySQL module installation fails**
A: Try:
```bash
pip install --upgrade setuptools
pip install mysqlclient
```

**Q12: Virtual environment won't activate**
A: Make sure you're in the correct directory:
```bash
cd C:\Users\YourUsername\Desktop\restaurant_delivery
venv\Scripts\activate
```

**Q13: Requirements.txt installation fails**
A: Try installing packages individually:
```bash
pip install Flask==2.3.2
pip install Flask-MySQLdb==1.0.1
pip install mysqlclient
pip install Werkzeug==2.3.6
```

**Q14: Port 5000 is already in use**
A: Modify app.py:
```python
app.run(debug=True, port=5001)  # Use different port
```

---

### Database Issues

**Q15: "Access denied for user 'root'"**
A: Check MySQL password in app.py:
```python
app.config['MYSQL_PASSWORD'] = 'your_password'
```
Make sure password matches MySQL root password set during installation.

**Q16: "Unknown database 'restaurant_delivery'"**
A: Database not created. Run SQL script:
```bash
mysql -u root -p < database/restaurant_delivery.sql
```

**Q17: "Can't connect to MySQL server"**
A: Ensure MySQL is running:
- Windows: Check MySQL service in Services
- Linux: `sudo systemctl start mysql`
- Mac: `mysql.server start`

**Q18: How do I reset the database?**
A: 
```sql
DROP DATABASE restaurant_delivery;
```
Then re-run the restaurant_delivery.sql script.

**Q19: How do I back up the database?**
A:
```bash
mysqldump -u root -p restaurant_delivery > backup.sql
```

**Q20: How do I restore from backup?**
A:
```bash
mysql -u root -p restaurant_delivery < backup.sql
```

---

### Application Issues

**Q21: App crashes on startup**
A: Check:
1. Is MySQL running?
2. Are database credentials correct in app.py?
3. Are all dependencies installed? `pip install -r requirements.txt`
4. Check console error messages

**Q22: "ModuleNotFoundError: No module named 'flask'"**
A: Make sure virtual environment is activated and dependencies are installed:
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

**Q23: Forms not submitting**
A: Check:
1. Browser console for JavaScript errors (F12)
2. Network tab for failed requests
3. Flask debug messages in terminal

**Q24: Database doesn't show sample data**
A: Sample data is inserted when SQL script runs. If missing:
1. Recreate database
2. Re-run SQL script
3. Verify script execution completed without errors

**Q25: Can't add customers/orders**
A: Check:
1. MySQL is running
2. Database is created
3. Credentials in app.py are correct
4. Check browser developer console for errors

---

### Features & Usage

**Q26: How do I delete a customer?**
A: Go to Customers page → Click "Delete" button next to customer

**Q27: How do I update delivery status?**
A: Go to Deliveries page → Click "Update" button → Update status and details

**Q28: Can customer feedback be modified?**
A: Not in current version. Would need database update directly, or code modification.

**Q29: How do I generate a report?**
A: Go to Reports menu → Select desired report (Daily, Staff Performance, Delayed Orders)

**Q30: Can I export reports?**
A: CSV export available through JavaScript function. PDF would need additional libraries.

---

### Performance & Optimization

**Q31: Application is running slowly**
A:
1. Check MySQL is running locally
2. Increase available RAM
3. Close other applications
4. Restart application

**Q32: Database queries are slow**
A:
1. Ensure indexes are created (they are by default)
2. Use filtering when possible
3. Reduce query complexity
4. Consider database optimization

**Q33: How many records can it handle?**
A: 
- Thousands of customers: No problem
- Millions of deliveries: May need optimization
- Current implementation works well for small to medium restaurants

**Q34: Can I run multiple instances?**
A: Yes, use different ports:
- Instance 1: Port 5000
- Instance 2: Port 5001
- etc.

---

### Customization & Development

**Q35: How do I add a new field to customers?**
A: 
1. Modify SQL: Add column to Customers table
2. Modify Flask: Update form input
3. Modify HTML template: Add form field
4. Test thoroughly

**Q36: How do I add a new report?**
A:
1. Create SQL query/view
2. Create Flask route in app.py
3. Create HTML template
4. Add navigation link

**Q37: Can I customize colors?**
A: Yes, modify `static/css/style.css`:
```css
/* Change purple theme */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* Modify to your colors */
```

**Q38: How do I change the application name?**
A:
1. Update app name in templates
2. Update navbar title
3. Update CSS styling

**Q39: How do I add user authentication?**
A: Requires:
1. User table in database
2. Flask-Login extension
3. Session management
4. Password hashing (werkzeug.security)

**Q40: Can I integrate with payment gateway?**
A: Yes, but requires:
1. Payment API integration
2. Stripe/PayPal/Razorpay SDK
3. Payment processing logic
4. Order modification

---

### Security

**Q41: Is the application secure?**
A: Basic security is implemented. For production, add:
- User authentication
- HTTPS/SSL
- Input validation
- CSRF protection
- Rate limiting
- SQL parameterization (already done)

**Q42: Should I change the SECRET_KEY?**
A: Yes! Change in app.py for production:
```python
app.secret_key = 'your-very-long-random-string-here'
```

**Q43: How do I protect sensitive data?**
A:
1. Use HTTPS in production
2. Hash passwords
3. Encrypt sensitive fields
4. Use environment variables for credentials
5. Implement access control

**Q44: Is SQL injection prevented?**
A: Yes! Parameterized queries are used throughout:
```python
cursor.execute('SELECT * FROM Customers WHERE customer_id = %s', (id,))
```

**Q45: How do I secure the database?**
A:
1. Set strong MySQL root password
2. Create db user with limited privileges
3. Remove default accounts
4. Regular backups
5. Update MySQL regularly

---

### Deployment

**Q46: How do I deploy to production?**
A:
1. Use WSGI server (Gunicorn, uWSGI)
2. Set DEBUG = False
3. Use environment variables for secrets
4. Set up HTTPS/SSL
5. Configure database backups
6. Set up monitoring

**Q47: Can I deploy to Heroku?**
A: Yes, with modifications:
1. Create Procfile
2. Add runtime.txt
3. Use PostgreSQL (recommended)
4. Modify database connection

**Q48: What's the hosting cost?**
A: Depends on provider:
- Heroku: $7+/month
- AWS: $5+/month (free tier available)
- DigitalOcean: $5+/month
- Shared hosting: $3-10/month

**Q49: Can I run on a VPS?**
A: Yes, fully compatible with:
- Linux VPS (Ubuntu recommended)
- Windows Server
- Any cloud provider supporting Python + MySQL

**Q50: How do I monitor the application?**
A:
1. Flask logging
2. Application Performance Monitoring (APM)
3. Database monitoring
4. Error tracking (Sentry)
5. Server monitoring

---

### Troubleshooting Guide

## Common Error Messages

### Error: "ModuleNotFoundError: No module named 'MySQLdb'"
**Cause**: MySQLdb not installed
**Solution**:
```bash
pip install mysqlclient
```

### Error: "OperationalError: (2003, "Can't connect to MySQL server")"
**Cause**: MySQL not running or wrong host/port
**Solution**:
1. Start MySQL service
2. Verify host and port in app.py
3. Check MySQL is listening on port 3306

### Error: "ProgrammingError: (1064, "You have an error in your SQL syntax")"
**Cause**: SQL syntax error in query
**Solution**:
1. Check SQL query syntax
2. Verify table/column names
3. Test query in MySQL Workbench

### Error: "ValueError: invalid literal for int()"
**Cause**: Type mismatch in input
**Solution**:
1. Add input validation
2. Check field types
3. Test with valid data

### Error: "404 Not Found"
**Cause**: Route doesn't exist
**Solution**:
1. Check URL spelling
2. Verify route exists in app.py
3. Check template links

### Error: "CSRF token missing"
**Cause**: Form token validation failed
**Solution**:
1. Include CSRF token in form
2. Clear browser cache
3. Restart application

---

## Debug Mode

Enable debug logging in app.py:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Check logs in:
1. Terminal output
2. app.log file (if configured)
3. Browser developer console
4. MySQL error log

---

## Performance Troubleshooting

### High CPU Usage
- Check for infinite loops
- Monitor database queries
- Reduce connection pool size
- Close unnecessary connections

### High Memory Usage
- Check for memory leaks
- Monitor large queries
- Limit result sets
- Use pagination

### Slow API Responses
- Enable query caching
- Add database indexes
- Optimize SQL queries
- Use connection pooling

---

## Getting Help

### Resources
1. Flask Documentation: https://flask.palletsprojects.com/
2. MySQL Documentation: https://dev.mysql.com/doc/
3. Stack Overflow: Tag your questions with 'flask' and 'mysql'
4. GitHub Issues: Report bugs

### When Reporting Issues
Include:
1. Error message (complete)
2. Python version (`python --version`)
3. OS (Windows/Linux/Mac)
4. Steps to reproduce
5. What you tried already

---

## Quick Reference

### Common Commands

```bash
# Activate virtual environment
venv\Scripts\activate

# Deactivate virtual environment
deactivate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Check Python version
python --version

# Check pip version
pip --version

# List installed packages
pip list

# Update pip
pip install --upgrade pip

# Connect to MySQL
mysql -u root -p

# Run SQL file
mysql -u root -p < database/restaurant_delivery.sql

# Export database
mysqldump -u root -p restaurant_delivery > backup.sql
```

---

## Useful Links

- Flask: https://flask.palletsprojects.com/
- MySQL: https://www.mysql.com/
- Python: https://www.python.org/
- Virtual Environments: https://docs.python.org/3/tutorial/venv.html
- Git: https://git-scm.com/

---

**Last Updated**: March 11, 2025
**Document Version**: 1.0

For more help, see README.md, SETUP_GUIDE.md, or API_DOCUMENTATION.md
