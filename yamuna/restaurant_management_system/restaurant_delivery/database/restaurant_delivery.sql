-- Restaurant Delivery Management System Database
-- Create Database
CREATE DATABASE IF NOT EXISTS restaurant_delivery;
USE restaurant_delivery;

-- =============================================
-- TABLE: Customers
-- =============================================
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =============================================
-- TABLE: DeliveryStaff
-- =============================================
CREATE TABLE IF NOT EXISTS DeliveryStaff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =============================================
-- TABLE: Orders
-- =============================================
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    order_time TIME NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending',
    order_amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- =============================================
-- TABLE: Delivery
-- =============================================
CREATE TABLE IF NOT EXISTS Delivery (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL UNIQUE,
    staff_id INT NOT NULL,
    delivery_date DATE NOT NULL,
    delivery_time TIME,
    delivery_status VARCHAR(50) DEFAULT 'Pending',
    feedback VARCHAR(500),
    rating INT CHECK (rating >= 1 AND rating <= 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES DeliveryStaff(staff_id) ON DELETE RESTRICT
);

-- =============================================
-- INSERT SAMPLE DATA
-- =============================================
INSERT INTO Customers (name, phone, address) VALUES
('Ravi Kumar', '9123456789', 'Guntur'),
('Priya Singh', '8234567890', 'Hyderabad'),
('Amit Patel', '7345678901', 'Bangalore'),
('Sneha Sharma', '6456789012', 'Mumbai'),
('Rahul Verma', '5567890123', 'Delhi');

INSERT INTO DeliveryStaff (name, phone, status) VALUES
('Ajay Kumar', '9876543210', 'Active'),
('Bhavesh Nair', '9876543211', 'Active'),
('Chirag Singh', '9876543212', 'Active'),
('Deepak Rao', '9876543213', 'Active');

INSERT INTO Orders (customer_id, order_date, order_time, status, order_amount) VALUES
(1, '2025-04-07', '12:30:00', 'Delivered', 500.00),
(2, '2025-04-07', '13:15:00', 'Delivered', 650.00),
(3, '2025-04-08', '14:00:00', 'Pending', 750.00),
(4, '2025-04-08', '15:45:00', 'Pending', 450.00),
(1, '2025-04-09', '12:00:00', 'Delivered', 800.00);

INSERT INTO Delivery (order_id, staff_id, delivery_date, delivery_time, delivery_status, feedback, rating) VALUES
(1, 1, '2025-04-07', '00:30:00', 'Delivered', 'Fast and good service', 5),
(2, 2, '2025-04-07', '00:45:00', 'Delivered', 'Good', 4),
(5, 1, '2025-04-09', '00:25:00', 'Delivered', 'Excellent delivery', 5);

-- =============================================
-- PROCEDURE: Assign Delivery Staff
-- =============================================
DELIMITER //

CREATE PROCEDURE AssignDeliveryStaff(
    IN p_order_id INT,
    IN p_staff_id INT,
    IN p_delivery_date DATE
)
BEGIN
    DECLARE v_staff_exists INT;
    DECLARE v_order_exists INT;
    
    -- Check if order exists
    SELECT COUNT(*) INTO v_order_exists FROM Orders WHERE order_id = p_order_id;
    IF v_order_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Order not found';
    END IF;
    
    -- Check if staff exists
    SELECT COUNT(*) INTO v_staff_exists FROM DeliveryStaff WHERE staff_id = p_staff_id;
    IF v_staff_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Staff not found';
    END IF;
    
    -- Insert delivery record
    INSERT INTO Delivery (order_id, staff_id, delivery_date, delivery_status)
    VALUES (p_order_id, p_staff_id, p_delivery_date, 'Assigned');
    
    UPDATE Orders SET status = 'In Transit' WHERE order_id = p_order_id;
END //

DELIMITER ;

-- =============================================
-- FUNCTION: Calculate Average Delivery Time
-- =============================================
DELIMITER //

CREATE FUNCTION CalculateAverageDeliveryTime(p_staff_id INT)
RETURNS DECIMAL(10, 2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_avg_time DECIMAL(10, 2);
    
    SELECT AVG(TIME_TO_SEC(delivery_time) / 60) INTO v_avg_time
    FROM Delivery
    WHERE staff_id = p_staff_id AND delivery_status = 'Delivered';
    
    RETURN IFNULL(v_avg_time, 0);
END //

DELIMITER ;

-- =============================================
-- PROCEDURE: Update Order Status
-- =============================================
DELIMITER //

CREATE PROCEDURE UpdateOrderStatus(
    IN p_order_id INT,
    IN p_new_status VARCHAR(50)
)
BEGIN
    DECLARE v_order_exists INT;
    
    SELECT COUNT(*) INTO v_order_exists FROM Orders WHERE order_id = p_order_id;
    IF v_order_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Order not found';
    END IF;
    
    UPDATE Orders 
    SET status = p_new_status 
    WHERE order_id = p_order_id;
    
    IF p_new_status = 'Delivered' THEN
        UPDATE Delivery 
        SET delivery_status = 'Delivered'
        WHERE order_id = p_order_id;
    END IF;
END //

DELIMITER ;

-- =============================================
-- VIEW: Daily Delivery Report
-- =============================================
CREATE OR REPLACE VIEW DailyDeliveryReport AS
SELECT 
    d.delivery_date,
    COUNT(d.delivery_id) AS total_deliveries,
    SUM(CASE WHEN d.delivery_status = 'Delivered' THEN 1 ELSE 0 END) AS completed_deliveries,
    SUM(CASE WHEN d.delivery_status = 'Pending' THEN 1 ELSE 0 END) AS pending_deliveries,
    AVG(CASE WHEN d.delivery_status = 'Delivered' THEN TIME_TO_SEC(d.delivery_time) / 60 END) AS avg_delivery_time_minutes
FROM Delivery d
GROUP BY d.delivery_date
ORDER BY d.delivery_date DESC;

-- =============================================
-- VIEW: Staff-wise Delivery Performance
-- =============================================
CREATE OR REPLACE VIEW StaffDeliveryPerformance AS
SELECT 
    ds.staff_id,
    ds.name,
    COUNT(d.delivery_id) AS total_deliveries,
    SUM(CASE WHEN d.delivery_status = 'Delivered' THEN 1 ELSE 0 END) AS completed_deliveries,
    ROUND(AVG(d.rating), 2) AS avg_rating,
    ROUND(AVG(CASE WHEN d.delivery_status = 'Delivered' THEN TIME_TO_SEC(d.delivery_time) / 60 END), 2) AS avg_delivery_time_mins
FROM DeliveryStaff ds
LEFT JOIN Delivery d ON ds.staff_id = d.staff_id
GROUP BY ds.staff_id, ds.name
ORDER BY completed_deliveries DESC;

-- =============================================
-- VIEW: Orders with Delayed Delivery
-- =============================================
CREATE OR REPLACE VIEW OrdersWithDelayedDelivery AS
SELECT 
    o.order_id,
    c.name AS customer_name,
    c.phone,
    o.order_date,
    d.delivery_date,
    d.delivery_time,
    ds.name AS staff_name,
    CASE 
        WHEN TIME_TO_SEC(d.delivery_time) / 60 > 45 THEN 'Delayed'
        ELSE 'On Time'
    END AS delivery_status
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Delivery d ON o.order_id = d.order_id
JOIN DeliveryStaff ds ON d.staff_id = ds.staff_id
ORDER BY d.delivery_date DESC;

-- =============================================
-- NESTED QUERIES
-- =============================================

-- 1. Orders not delivered within 30 minutes
SELECT 
    o.order_id,
    c.name AS customer_name,
    ds.name AS staff_name,
    d.delivery_time,
    (SELECT COUNT(*) FROM Delivery WHERE TIME_TO_SEC(delivery_time) / 60 > 30) AS delayed_count
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Delivery d ON o.order_id = d.order_id
JOIN DeliveryStaff ds ON d.staff_id = ds.staff_id
WHERE TIME_TO_SEC(d.delivery_time) / 60 > 30;

-- 2. Staff with most deliveries
SELECT ds.staff_id, ds.name, COUNT(d.delivery_id) AS delivery_count
FROM DeliveryStaff ds
LEFT JOIN Delivery d ON ds.staff_id = d.staff_id
GROUP BY ds.staff_id, ds.name
HAVING COUNT(d.delivery_id) >= (
    SELECT COUNT(delivery_id) / COUNT(DISTINCT staff_id)
    FROM Delivery
)
ORDER BY delivery_count DESC;

-- 3. Customer with highest orders
SELECT c.customer_id, c.name, c.phone, COUNT(o.order_id) AS order_count
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name, c.phone
HAVING COUNT(o.order_id) >= (
    SELECT COUNT(order_id) / COUNT(DISTINCT customer_id)
    FROM Orders
)
ORDER BY order_count DESC;

-- =============================================
-- JOIN BASED QUERIES
-- =============================================

-- 1. Order and delivery status
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
ORDER BY o.order_date DESC;

-- 2. Delivery summary by date
SELECT 
    d.delivery_date,
    COUNT(d.delivery_id) AS total_deliveries,
    SUM(o.order_amount) AS total_amount,
    COUNT(DISTINCT d.staff_id) AS staff_involved
FROM Delivery d
JOIN Orders o ON d.order_id = o.order_id
GROUP BY d.delivery_date
ORDER BY d.delivery_date DESC;

-- 3. Staff-wise delivery count
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
ORDER BY total_deliveries DESC;
