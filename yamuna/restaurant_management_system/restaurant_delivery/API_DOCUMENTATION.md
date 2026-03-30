# Restaurant Delivery Management System - API Documentation

Complete API reference for the Restaurant Delivery Management System.

## Base URL
```
http://localhost:5000
```

## Authentication
Currently, the system does not require authentication. This should be implemented for production use.

---

## 1. PAGES & VIEWS

### Home Page
```
GET /
```
Returns the home page with system overview and features.

**Response**: HTML Page

---

### Dashboard
```
GET /dashboard
```
Returns the dashboard with system statistics.

**Response**: HTML Page with:
- Total Customers
- Total Orders
- Completed Deliveries
- Active Staff
- Average Rating

---

## 2. CUSTOMER ENDPOINTS

### Get All Customers
```
GET /customers
```
Returns all customers with a form to add new customers.

**Response**: HTML Page with customer list

**Sample Data**:
```json
{
  "customer_id": 1,
  "name": "Ravi Kumar",
  "phone": "9123456789",
  "address": "Guntur"
}
```

---

### Add New Customer
```
POST /customers
Content-Type: application/json
```

**Request Body**:
```json
{
  "name": "John Doe",
  "phone": "9876543210",
  "address": "123 Main Street"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Customer added successfully"
}
```

---

### Get Customer Orders
```
GET /customer/<id>/orders
```
Returns all orders for a specific customer.

**Path Parameters**:
- `id` (required): Customer ID

**Response**: HTML Page with customer details and orders

---

### Delete Customer
```
POST /customer/<id>/delete
```
Deletes a customer and all associated orders.

**Path Parameters**:
- `id` (required): Customer ID

**Response**:
```json
{
  "success": true,
  "message": "Customer deleted successfully"
}
```

---

## 3. ORDER ENDPOINTS

### Get All Orders
```
GET /orders
```
Returns all orders with ability to create new ones.

**Response**: HTML Page with orders list

**Sample Order Data**:
```json
{
  "order_id": 101,
  "customer_id": 1,
  "order_date": "2025-04-07",
  "order_time": "12:30:00",
  "status": "Delivered",
  "order_amount": 500.00,
  "customer_name": "Ravi Kumar"
}
```

---

### Create New Order
```
POST /orders
Content-Type: application/json
```

**Request Body**:
```json
{
  "customer_id": 1,
  "order_amount": 599.99
}
```

**Response**:
```json
{
  "success": true,
  "message": "Order created successfully"
}
```

---

### Update Order Status
```
PUT /order/<id>/status
Content-Type: application/json
```

**Path Parameters**:
- `id` (required): Order ID

**Request Body**:
```json
{
  "status": "Delivered"
}
```

**Status Options**: `Pending`, `In Transit`, `Delivered`

**Response**:
```json
{
  "success": true,
  "message": "Order status updated"
}
```

---

## 4. STAFF ENDPOINTS

### Get All Staff
```
GET /staff
```
Returns all delivery staff members.

**Response**: HTML Page with staff list

**Sample Staff Data**:
```json
{
  "staff_id": 1,
  "name": "Ajay Kumar",
  "phone": "9876543210",
  "status": "Active"
}
```

---

### Add New Staff
```
POST /staff
Content-Type: application/json
```

**Request Body**:
```json
{
  "name": "Rahul Singh",
  "phone": "9876543211"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Staff added successfully"
}
```

---

### Delete Staff
```
POST /staff/<id>/delete
```
Deletes a staff member.

**Path Parameters**:
- `id` (required): Staff ID

**Response**:
```json
{
  "success": true,
  "message": "Staff deleted successfully"
}
```

---

## 5. DELIVERY ENDPOINTS

### Get All Deliveries
```
GET /deliveries
```
Returns all deliveries with assignment form.

**Response**: HTML Page with deliveries list

**Sample Delivery Data**:
```json
{
  "delivery_id": 1,
  "order_id": 101,
  "staff_id": 1,
  "delivery_date": "2025-04-07",
  "delivery_time": "00:30:00",
  "delivery_status": "Delivered",
  "feedback": "Fast and good service",
  "rating": 5,
  "customer_name": "Ravi Kumar",
  "staff_name": "Ajay Kumar"
}
```

---

### Assign Delivery
```
POST /deliveries
Content-Type: application/json
```

**Request Body**:
```json
{
  "order_id": 103,
  "staff_id": 2,
  "delivery_date": "2025-04-10"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Delivery assigned successfully"
}
```

---

### Update Delivery
```
PUT /delivery/<id>/update
Content-Type: application/json
```

**Path Parameters**:
- `id` (required): Delivery ID

**Request Body**:
```json
{
  "delivery_status": "Delivered",
  "delivery_time": "00:35:00",
  "feedback": "Good delivery service",
  "rating": 4
}
```

**Delivery Status Options**: `Pending`, `In Transit`, `Delivered`, `Cancelled`

**Rating**: 1-5 (integer)

**Response**:
```json
{
  "success": true,
  "message": "Delivery updated successfully"
}
```

---

## 6. REPORT ENDPOINTS

### Daily Delivery Report
```
GET /reports/daily
```
Returns daily delivery statistics.

**Response**: HTML Page with:
- Date
- Total Deliveries
- Completed Deliveries
- Pending Deliveries
- Average Delivery Time

---

### Staff Performance Report
```
GET /reports/staff-performance
```
Returns staff performance metrics.

**Response**: HTML Page with:
- Staff ID
- Name
- Total Deliveries
- Completed Deliveries
- Average Rating
- Average Delivery Time

---

### Delayed Orders Report
```
GET /reports/delayed-orders
```
Returns orders with delivery time > 45 minutes.

**Response**: HTML Page with:
- Order ID
- Customer Name
- Phone
- Delivery Date & Time
- Staff Name
- Status (Delayed/On Time)

---

## 7. ANALYTICS API ENDPOINTS (JSON)

### Orders Not Delivered Within 30 Minutes
```
GET /api/orders-not-delivered-30mins
```

**Response**:
```json
{
  "success": true,
  "data": [
    {
      "order_id": 101,
      "customer_name": "Ravi Kumar",
      "staff_name": "Ajay Kumar",
      "delivery_time": "00:35:00",
      "minutes": 35
    }
  ]
}
```

---

### Staff with Most Deliveries
```
GET /api/staff-most-deliveries
```

**Response**:
```json
{
  "success": true,
  "data": [
    {
      "staff_id": 1,
      "name": "Ajay Kumar",
      "delivery_count": 15
    }
  ]
}
```

---

### Customer with Highest Orders
```
GET /api/customer-highest-orders
```

**Response**:
```json
{
  "success": true,
  "data": [
    {
      "customer_id": 1,
      "name": "Ravi Kumar",
      "phone": "9123456789",
      "order_count": 5
    }
  ]
}
```

---

### Order and Delivery Status
```
GET /api/order-delivery-status
```

**Response**:
```json
{
  "success": true,
  "data": [
    {
      "order_id": 101,
      "customer_name": "Ravi Kumar",
      "order_date": "2025-04-07",
      "order_status": "Delivered",
      "delivery_date": "2025-04-07",
      "delivery_status": "Delivered",
      "staff_name": "Ajay Kumar"
    }
  ]
}
```

---

### Delivery Summary by Date
```
GET /api/delivery-summary-by-date
```

**Response**:
```json
{
  "success": true,
  "data": [
    {
      "delivery_date": "2025-04-09",
      "total_deliveries": 5,
      "total_amount": 2500.00,
      "staff_involved": 3
    }
  ]
}
```

---

### Staff Delivery Count
```
GET /api/staff-delivery-count
```

**Response**:
```json
{
  "success": true,
  "data": [
    {
      "staff_id": 1,
      "name": "Ajay Kumar",
      "phone": "9876543210",
      "total_deliveries": 12,
      "completed": 10,
      "avg_rating": 4.5
    }
  ]
}
```

---

### Average Delivery Time for Staff
```
GET /reports/average-delivery-time/<staff_id>
```

**Path Parameters**:
- `staff_id` (required): Staff ID

**Response**:
```json
{
  "success": true,
  "avg_time": 32.45
}
```

---

## Error Responses

### 404 Not Found
```json
{
  "success": false,
  "message": "Resource not found"
}
```

### 400 Bad Request
```json
{
  "success": false,
  "message": "Invalid request parameters"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "message": "An error occurred while processing your request"
}
```

---

## Data Validation Rules

### Customer
- Name: Required, max 100 characters
- Phone: Required, unique, 10-15 digits
- Address: Required, max 255 characters

### Order
- Customer ID: Required, must exist
- Order Amount: Required, positive decimal
- Order Date: Automatically set to current date
- Status: Defaults to "Pending"

### Staff
- Name: Required, max 100 characters
- Phone: Required, unique, 10-15 digits
- Status: Defaults to "Active"

### Delivery
- Order ID: Required, must exist, unique
- Staff ID: Required, must exist
- Delivery Date: Required
- Delivery Time: Optional (HH:MM:SS format)
- Delivery Status: Defaults to "Assigned"
- Rating: Optional, must be 1-5 if provided

---

## Rate Limiting

Currently, no rate limiting is implemented. This should be added for production use.

---

## CORS

Currently, CORS is disabled. Enable if needed for external API access.

---

## Database Functions (SQL)

### Calculate Average Delivery Time
```sql
SELECT CalculateAverageDeliveryTime(staff_id) as avg_time;
```

### Assign Delivery Staff
```sql
CALL AssignDeliveryStaff(order_id, staff_id, delivery_date);
```

### Update Order Status
```sql
CALL UpdateOrderStatus(order_id, new_status);
```

---

## Database Views

### Daily Delivery Report
```sql
SELECT * FROM DailyDeliveryReport;
```

### Staff Performance
```sql
SELECT * FROM StaffDeliveryPerformance;
```

### Orders with Delayed Delivery
```sql
SELECT * FROM OrdersWithDelayedDelivery;
```

---

## Pagination

Default items per page: 10

To implement pagination for list endpoints, modify the routes in `app.py`.

---

## Sorting

Default sorting is by date descending. To customize:
1. Modify SQL queries in `app.py`
2. Add query parameters for sort field and order

---

## Search

Global search is not yet implemented. Can be added by:
1. Modifying front-end JavaScript
2. Adding search SQL queries in backend

---

## Export Formats

- CSV export available via JavaScript in frontend
- PDF export can be implemented using Flask extensions
- JSON export via API endpoints

---

## Webhooks

Not currently implemented. Can be added for:
- Delivery status updates
- Customer notifications
- Integration with external systems

---

## API Versioning

Current version: v1

Future versions can be managed by:
- URL: `/api/v2/...`
- Headers: `Accept: application/vnd.api+json;version=2`

---

## Future Enhancements

- [ ] OAuth 2.0 authentication
- [ ] API key management
- [ ] Rate limiting
- [ ] Caching headers
- [ ] GraphQL endpoint
- [ ] WebSocket for real-time updates
- [ ] Comprehensive API testing suite

---

## Support

For API issues or questions, refer to:
- README.md
- SETUP_GUIDE.md
- Flask-MySQLdb documentation

---

**API Documentation Version**: 1.0
**Last Updated**: March 11, 2025
