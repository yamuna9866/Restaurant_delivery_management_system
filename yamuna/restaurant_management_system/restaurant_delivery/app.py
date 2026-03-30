from flask import Flask, render_template, request, jsonify
import MySQLdb
import MySQLdb.cursors
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# MySQL Configuration - EDIT THESE FOR YOUR DATABASE
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'  # Change to your MySQL root password
MYSQL_DB = 'restaurant_delivery'

def get_db_connection():
    """Create a new database connection"""
    try:
        conn = MySQLdb.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            db=MYSQL_DB,
            cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf8mb4'
        )
        return conn
    except MySQLdb.Error as e:
        print(f"Database connection error: {e}")
        return None

# =============================================
# HOME & DASHBOARD ROUTES
# =============================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers', methods=['GET', 'POST'])
def manage_customers():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        phone = data.get('phone')
        address = data.get('address')
        
        conn = get_db_connection()
        if not conn:
            return jsonify({'success': False, 'message': 'Database connection failed'})
        
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Customers (name, phone, address) VALUES (%s, %s, %s)', 
                         (name, phone, address))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'success': True, 'message': 'Customer added successfully'})
        except Exception as e:
            cursor.close()
            conn.close()
            return jsonify({'success': False, 'message': str(e)})
    
    conn = get_db_connection()
    if not conn:
        customers = []
    else:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Customers')
            customers = cursor.fetchall()
            cursor.close()
            conn.close()
        except:
            customers = []
    
    return render_template('customers.html', customers=customers)

@app.route('/customer/<int:customer_id>/orders')
def customer_orders(customer_id):
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT o.*, c.name as customer_name 
            FROM Orders o 
            JOIN Customers c ON o.customer_id = c.customer_id 
            WHERE o.customer_id = %s
            ORDER BY o.order_date DESC
        ''', (customer_id,))
        orders = cursor.fetchall()
        
        cursor.execute('SELECT * FROM Customers WHERE customer_id = %s', (customer_id,))
        customer = cursor.fetchone()
        
        cursor.close()
        conn.close()
        return render_template('customer_orders.html', customer=customer, orders=orders)
    except Exception as e:
        cursor.close()
        conn.close()
        return f"Error: {str(e)}", 500

@app.route('/customer/<int:customer_id>/delete', methods=['POST'])
def delete_customer(customer_id):
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Customers WHERE customer_id = %s', (customer_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'message': 'Customer deleted successfully'})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

# =============================================
# ORDER ROUTES
# =============================================

@app.route('/orders', methods=['GET', 'POST'])
def manage_orders():
    if request.method == 'POST':
        data = request.get_json()
        customer_id = data.get('customer_id')
        order_amount = data.get('order_amount')
        
        conn = get_db_connection()
        if not conn:
            return jsonify({'success': False, 'message': 'Database connection failed'})
        
        try:
            cursor = conn.cursor()
            order_date = datetime.now().date()
            order_time = datetime.now().time()
            cursor.execute('''
                INSERT INTO Orders (customer_id, order_date, order_time, order_amount, status)
                VALUES (%s, %s, %s, %s, 'Pending')
            ''', (customer_id, order_date, order_time, order_amount))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'success': True, 'message': 'Order created successfully'})
        except Exception as e:
            cursor.close()
            conn.close()
            return jsonify({'success': False, 'message': str(e)})
    
    conn = get_db_connection()
    if not conn:
        return render_template('orders.html', orders=[], customers=[])
    
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Customers')
        customers = cursor.fetchall()
        
        cursor.execute('''
            SELECT o.*, c.name as customer_name 
            FROM Orders o 
            JOIN Customers c ON o.customer_id = c.customer_id
            ORDER BY o.order_date DESC
        ''')
        orders = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return render_template('orders.html', orders=orders, customers=customers)
    except Exception as e:
        cursor.close()
        conn.close()
        return render_template('orders.html', orders=[], customers=[])

@app.route('/order/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    data = request.get_json()
    new_status = data.get('status')
    
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('CALL UpdateOrderStatus(%s, %s)', (order_id, new_status))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'message': 'Order status updated'})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

# =============================================
# DELIVERY STAFF ROUTES
# =============================================

@app.route('/staff', methods=['GET', 'POST'])
def manage_staff():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        phone = data.get('phone')
        
        conn = get_db_connection()
        if not conn:
            return jsonify({'success': False, 'message': 'Database connection failed'})
        
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO DeliveryStaff (name, phone, status) VALUES (%s, %s, "Active")', 
                         (name, phone))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'success': True, 'message': 'Staff added successfully'})
        except Exception as e:
            cursor.close()
            conn.close()
            return jsonify({'success': False, 'message': str(e)})
    
    conn = get_db_connection()
    if not conn:
        staff = []
    else:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM DeliveryStaff')
            staff = cursor.fetchall()
            cursor.close()
            conn.close()
        except:
            staff = []
    
    return render_template('staff.html', staff=staff)

@app.route('/staff/<int:staff_id>/delete', methods=['POST'])
def delete_staff(staff_id):
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM DeliveryStaff WHERE staff_id = %s', (staff_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'message': 'Staff deleted successfully'})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

# =============================================
# DELIVERY ROUTES
# =============================================

@app.route('/deliveries', methods=['GET', 'POST'])
def manage_deliveries():
    if request.method == 'POST':
        data = request.get_json()
        order_id = data.get('order_id')
        staff_id = data.get('staff_id')
        delivery_date = data.get('delivery_date')
        
        conn = get_db_connection()
        if not conn:
            return jsonify({'success': False, 'message': 'Database connection failed'})
        
        try:
            cursor = conn.cursor()
            cursor.execute('CALL AssignDeliveryStaff(%s, %s, %s)', 
                         (order_id, staff_id, delivery_date))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'success': True, 'message': 'Delivery assigned successfully'})
        except Exception as e:
            cursor.close()
            conn.close()
            return jsonify({'success': False, 'message': str(e)})
    
    conn = get_db_connection()
    if not conn:
        return render_template('deliveries.html', deliveries=[], pending_orders=[], staff=[])
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT d.*, o.order_id, c.name as customer_name, ds.name as staff_name
            FROM Delivery d
            JOIN Orders o ON d.order_id = o.order_id
            JOIN Customers c ON o.customer_id = c.customer_id
            JOIN DeliveryStaff ds ON d.staff_id = ds.staff_id
            ORDER BY d.delivery_date DESC
        ''')
        deliveries = cursor.fetchall()
        
        cursor.execute('SELECT order_id, customer_id FROM Orders WHERE status = "Pending"')
        pending_orders = cursor.fetchall()
        
        cursor.execute('SELECT * FROM DeliveryStaff WHERE status = "Active"')
        staff = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return render_template('deliveries.html', deliveries=deliveries, pending_orders=pending_orders, staff=staff)
    except Exception as e:
        cursor.close()
        conn.close()
        return render_template('deliveries.html', deliveries=[], pending_orders=[], staff=[])

@app.route('/delivery/<int:delivery_id>/update', methods=['PUT'])
def update_delivery(delivery_id):
    data = request.get_json()
    delivery_status = data.get('delivery_status')
    delivery_time = data.get('delivery_time')
    feedback = data.get('feedback')
    rating = data.get('rating')
    
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Delivery 
            SET delivery_status = %s, delivery_time = %s, feedback = %s, rating = %s
            WHERE delivery_id = %s
        ''', (delivery_status, delivery_time, feedback, rating, delivery_id))
        
        if delivery_status == 'Delivered':
            cursor.execute('''
                UPDATE Orders
                SET status = 'Delivered'
                WHERE order_id = (SELECT order_id FROM Delivery WHERE delivery_id = %s)
            ''', (delivery_id,))
        
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'message': 'Delivery updated successfully'})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

# =============================================
# REPORTS AND ANALYTICS ROUTES
# =============================================

@app.route('/reports/daily')
def daily_delivery_report():
    conn = get_db_connection()
    if not conn:
        return render_template('daily_report.html', reports=[])
    
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM DailyDeliveryReport')
        daily_reports = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('daily_report.html', reports=daily_reports)
    except Exception as e:
        cursor.close()
        conn.close()
        return render_template('daily_report.html', reports=[])

@app.route('/reports/staff-performance')
def staff_performance():
    conn = get_db_connection()
    if not conn:
        return render_template('staff_performance.html', performance=[])
    
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM StaffDeliveryPerformance')
        staff_performance = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('staff_performance.html', performance=staff_performance)
    except Exception as e:
        cursor.close()
        conn.close()
        return render_template('staff_performance.html', performance=[])

@app.route('/reports/delayed-orders')
def delayed_orders():
    conn = get_db_connection()
    if not conn:
        return render_template('delayed_orders.html', delayed_orders=[])
    
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM OrdersWithDelayedDelivery')
        delayed = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('delayed_orders.html', delayed_orders=delayed)
    except Exception as e:
        cursor.close()
        conn.close()
        return render_template('delayed_orders.html', delayed_orders=[])

@app.route('/reports/average-delivery-time/<int:staff_id>')
def average_delivery_time(staff_id):
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT CalculateAverageDeliveryTime(%s) as avg_time', (staff_id,))
        result = cursor.fetchone()
        avg_time = result['avg_time'] if result else 0
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'avg_time': avg_time})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/orders-not-delivered-30mins')
def orders_not_delivered_30():
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                o.order_id,
                c.name AS customer_name,
                ds.name AS staff_name,
                d.delivery_time,
                TIME_TO_SEC(d.delivery_time) / 60 AS minutes
            FROM Orders o
            JOIN Customers c ON o.customer_id = c.customer_id
            JOIN Delivery d ON o.order_id = d.order_id
            JOIN DeliveryStaff ds ON d.staff_id = ds.staff_id
            WHERE TIME_TO_SEC(d.delivery_time) / 60 > 30
        ''')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/staff-most-deliveries')
def staff_most_deliveries():
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT ds.staff_id, ds.name, COUNT(d.delivery_id) AS delivery_count
            FROM DeliveryStaff ds
            LEFT JOIN Delivery d ON ds.staff_id = d.staff_id
            GROUP BY ds.staff_id, ds.name
            ORDER BY delivery_count DESC
        ''')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/customer-highest-orders')
def customer_highest_orders():
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.customer_id, c.name, c.phone, COUNT(o.order_id) AS order_count
            FROM Customers c
            LEFT JOIN Orders o ON c.customer_id = o.customer_id
            GROUP BY c.customer_id, c.name, c.phone
            ORDER BY order_count DESC
        ''')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/order-delivery-status')
def order_delivery_status():
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                o.order_id,
                c.name AS customer_name,
                o.order_date,
                o.status AS order_status,
                d.delivery_date,
                d.delivery_status,
                ds.name AS staff_name
            FROM Orders o
            LEFT JOIN Customers c ON o.customer_id = c.customer_id
            LEFT JOIN Delivery d ON o.order_id = d.order_id
            LEFT JOIN DeliveryStaff ds ON d.staff_id = ds.staff_id
            ORDER BY o.order_date DESC
        ''')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/delivery-summary-by-date')
def delivery_summary_by_date():
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                d.delivery_date,
                COUNT(d.delivery_id) AS total_deliveries,
                SUM(o.order_amount) AS total_amount,
                COUNT(DISTINCT d.staff_id) AS staff_involved
            FROM Delivery d
            JOIN Orders o ON d.order_id = o.order_id
            GROUP BY d.delivery_date
            ORDER BY d.delivery_date DESC
        ''')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/staff-delivery-count')
def staff_delivery_count():
    conn = get_db_connection()
    if not conn:
        return jsonify({'success': False, 'message': 'Database connection failed'})
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                ds.staff_id,
                ds.name,
                ds.phone,
                COUNT(d.delivery_id) AS total_deliveries,
                COUNT(CASE WHEN d.delivery_status = 'Delivered' THEN 1 END) AS completed,
                ROUND(AVG(d.rating), 2) AS avg_rating
            FROM DeliveryStaff ds
            LEFT JOIN Delivery d ON ds.staff_id = d.staff_id
            GROUP BY ds.staff_id, ds.name, ds.phone
            ORDER BY total_deliveries DESC
        ''')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': str(e)})

# =============================================
# DASHBOARD ROUTE
# =============================================

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
    
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT COUNT(*) as count FROM Customers')
        total_customers = cursor.fetchone()['count']
        
        cursor.execute('SELECT COUNT(*) as count FROM Orders')
        total_orders = cursor.fetchone()['count']
        
        cursor.execute('SELECT COUNT(*) as count FROM Delivery WHERE delivery_status = "Delivered"')
        completed_deliveries = cursor.fetchone()['count']
        
        cursor.execute('SELECT COUNT(*) as count FROM DeliveryStaff WHERE status = "Active"')
        active_staff = cursor.fetchone()['count']
        
        cursor.execute('SELECT AVG(rating) as avg FROM Delivery WHERE rating IS NOT NULL')
        result = cursor.fetchone()
        avg_rating = result['avg'] if result['avg'] else 0
        
        cursor.close()
        conn.close()
        
        return render_template('dashboard.html', 
                             total_customers=total_customers,
                             total_orders=total_orders,
                             completed_deliveries=completed_deliveries,
                             active_staff=active_staff,
                             avg_rating=round(avg_rating, 2))
    except Exception as e:
        cursor.close()
        conn.close()
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
