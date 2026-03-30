# Restaurant Delivery Management System - Quick Reference Card

## 🚀 Quick Start (5 Minutes)

### Windows
```bash
cd restaurant_delivery
run.bat
```

### Linux/Mac
```bash
cd restaurant_delivery
bash run.sh
```

### Manual
```bash
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/Mac
pip install -r requirements.txt
python app.py
```

→ Open http://localhost:5000

---

## 📂 File Structure at a Glance

```
app.py              ← Main application (start here)
requirements.txt    ← Python packages
config.py          ← Configuration settings
database/          
  └── *.sql        ← Database schema
templates/
  └── *.html       ← Web pages
static/
  ├── css/style.css    ← Styling
  └── js/script.js     ← Interactions
```

---

## 🔑 Key Routes

| Route | Purpose |
|-------|---------|
| `/` | Home page |
| `/dashboard` | Dashboard |
| `/customers` | Customer management |
| `/orders` | Order management |
| `/staff` | Staff management |
| `/deliveries` | Delivery management |
| `/reports/*` | Various reports |

---

## 📊 Database Tables

| Table | Purpose |
|-------|---------|
| `Customers` | Customer info |
| `Orders` | Order details |
| `DeliveryStaff` | Staff info |
| `Delivery` | Delivery tracking |

---

## 🔧 Configuration

Edit `app.py` lines 14-18:
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'restaurant_delivery'
```

---

## 💾 Database Setup

```bash
# Create database
mysql -u root -p < database/restaurant_delivery.sql

# Verify
mysql -u root -p
SHOW DATABASES;
USE restaurant_delivery;
SHOW TABLES;
SELECT * FROM Customers;
```

---

## 🌐 Common URLs

| URL | Description |
|-----|-------------|
| http://localhost:5000 | Home page |
| http://localhost:5000/dashboard | Dashboard |
| http://localhost:5000/customers | Customers |
| http://localhost:5000/orders | Orders |
| http://localhost:5000/staff | Staff |
| http://localhost:5000/deliveries | Deliveries |
| http://localhost:5000/reports/daily | Daily report |

---

## 🐛 Common Issues

| Issue | Fix |
|-------|-----|
| Python not found | Add to PATH, restart terminal |
| MySQL not found | Install MySQL Server |
| Module not found | `pip install -r requirements.txt` |
| Port 5000 in use | Change port in app.py line 274 |
| Database not found | Run SQL script: `mysql -u root -p < database/restaurant_delivery.sql` |
| Can't connect to DB | Check password in app.py line 14-18 |

---

## 📚 Documentation Files

| File | Contains |
|------|----------|
| `README.md` | Project overview |
| `SETUP_GUIDE.md` | Detailed setup |
| `API_DOCUMENTATION.md` | All endpoints |
| `FAQ_TROUBLESHOOTING.md` | Common issues |
| `PROJECT_SUMMARY.md` | Complete details |

---

## 🎨 Customize Colors

Edit `static/css/style.css`:
```css
/* Find and modify gradient colors */
background: linear-gradient(135deg, #NEW_COLOR1 0%, #NEW_COLOR2 100%);
```

---

## 📝 Database Functions

```sql
-- Calculate average delivery time
SELECT CalculateAverageDeliveryTime(staff_id);

-- Assign delivery
CALL AssignDeliveryStaff(order_id, staff_id, delivery_date);

-- Update order status
CALL UpdateOrderStatus(order_id, new_status);
```

---

## 🔒 Security (Production)

```python
# Change this in app.py
app.secret_key = 'CHANGE_THIS_TO_RANDOM_STRING'

# Set to False
app.run(debug=False)
```

---

## 📦 Add New Dependencies

```bash
pip install package_name
pip freeze > requirements.txt
```

---

## 🧪 Test the Database

```sql
-- Check sample data
SELECT * FROM Customers;

-- Check orders
SELECT * FROM Orders;

-- Check deliveries
SELECT * FROM Delivery;

-- View daily report
SELECT * FROM DailyDeliveryReport;
```

---

## 🚀 Deploy to Heroku

1. Create `Procfile`:
```
web: gunicorn app:app
```

2. Add `runtime.txt`:
```
python-3.9.16
```

3. Deploy:
```bash
heroku create app-name
git push heroku main
```

---

## 🖥️ System Requirements

✓ Python 3.7+
✓ MySQL 5.7+
✓ 256MB RAM
✓ 500MB disk
✓ Modern browser

---

## ⚙️ Python Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Deactivate
deactivate

# Check (should show (venv))
echo %VIRTUAL_ENV%
```

---

## 🔄 Workflow

1. **Setup**: Run SETUP_GUIDE.md steps
2. **Start**: `python app.py`
3. **Access**: http://localhost:5000
4. **Use**: Add customers → Create orders → Assign deliveries → Track

---

## 👥 Sample Data

- 5 Customers
- 4 Staff members
- 5 Orders
- 3 Deliveries with ratings

---

## 📱 Responsive Design

✓ Works on Desktop
✓ Tablet friendly
✓ Mobile optimized (CSS Grid/Flexbox)

---

## 📊 Built-in Reports

- Daily Delivery Report
- Staff Performance Report
- Delayed Orders Report

---

## 🔌 API Endpoints (JSON)

```
GET  /api/orders-not-delivered-30mins
GET  /api/staff-most-deliveries
GET  /api/customer-highest-orders
GET  /api/order-delivery-status
GET  /api/delivery-summary-by-date
GET  /api/staff-delivery-count
```

---

## 🆘 Emergency Fixes

```bash
# Restart everything
deactivate
rm -r venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## 📞 Quick Help

1. **Setup issues**: See `SETUP_GUIDE.md`
2. **API issues**: See `API_DOCUMENTATION.md`
3. **Common errors**: See `FAQ_TROUBLESHOOTING.md`
4. **Project info**: See `README.md`

---

## 🎯 Next Steps

1. ✅ Run application
2. ✅ Add a customer
3. ✅ Create an order
4. ✅ Add staff member
5. ✅ Assign delivery
6. ✅ View reports
7. ✅ Customize styling

---

## 📝 Code Snippets

### Add Customer (Python)
```python
cursor.execute(
    'INSERT INTO Customers (name, phone, address) VALUES (%s, %s, %s)',
    (name, phone, address)
)
mysql.connection.commit()
```

### Get Orders (SQL)
```sql
SELECT o.*, c.name as customer_name 
FROM Orders o 
JOIN Customers c ON o.customer_id = c.customer_id;
```

### Update Status (JavaScript)
```javascript
fetch('/order/' + orderId + '/status', {
    method: 'PUT',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({status: 'Delivered'})
})
```

---

## 🏆 Features

✨ Full customer management
✨ Order tracking
✨ Staff management
✨ Real-time delivery updates
✨ Customer feedback & ratings
✨ Advanced reporting
✨ Database procedures & functions
✨ Responsive UI

---

## 🚀 Performance Tips

- Keep MySQL running
- Use Chrome/Firefox browser
- Minimize open applications
- Archive old data regularly
- Monitor database size

---

## ✅ Checklist

- [ ] Python installed
- [ ] MySQL running
- [ ] Virtual environment active
- [ ] Dependencies installed
- [ ] Database created
- [ ] Credentials correct
- [ ] Application running
- [ ] Can access http://localhost:5000

---

**Version**: 1.0
**Last Updated**: March 11, 2025
**Ready to use!** 🎉
