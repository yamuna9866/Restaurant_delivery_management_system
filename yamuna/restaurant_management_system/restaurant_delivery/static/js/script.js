// =============================================
// GENERAL UTILITIES
// =============================================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize any tooltips or dropdowns
    initializeUI();
});

function initializeUI() {
    // Any general UI initialization can go here
    console.log('Restaurant Delivery Management System Loaded');
}

// =============================================
// MODAL FUNCTIONS
// =============================================

function showModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
    }
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}

// =============================================
// CUSTOMER FUNCTIONS
// =============================================

function deleteCustomer(customerId) {
    if (confirm('Are you sure you want to delete this customer? This will also delete all their orders.')) {
        fetch('/customer/' + customerId + '/delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Customer deleted successfully!');
                location.reload();
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while deleting the customer');
        });
    }
}

// =============================================
// ORDER FUNCTIONS
// =============================================

function updateStatus(orderId, newStatus) {
    if (!newStatus) return;
    
    fetch('/order/' + orderId + '/status', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status: newStatus })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Order status updated!');
            location.reload();
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred');
    });
}

// =============================================
// DELIVERY FUNCTIONS
// =============================================

function showUpdateForm(deliveryId) {
    document.getElementById('delivery_id_update').value = deliveryId;
    const modal = document.getElementById('updateModal');
    if (modal) {
        modal.style.display = 'block';
    }
}

function updateDelivery() {
    const deliveryId = document.getElementById('delivery_id_update').value;
    const deliveryStatus = document.getElementById('delivery_status').value;
    const deliveryTimeRaw = document.getElementById('delivery_time_update').value;
    const feedback = document.getElementById('feedback_update').value;
    const rating = document.getElementById('rating_update').value;
    
    // Convert minutes to TIME format (HH:MM:SS)
    let deliveryTime = null;
    if (deliveryTimeRaw) {
        const minutes = parseInt(deliveryTimeRaw);
        const hours = Math.floor(minutes / 60);
        const mins = minutes % 60;
        deliveryTime = String(hours).padStart(2, '0') + ':' + String(mins).padStart(2, '0') + ':00';
    }
    
    fetch('/delivery/' + deliveryId + '/update', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            delivery_status: deliveryStatus,
            delivery_time: deliveryTime,
            feedback: feedback,
            rating: rating ? parseInt(rating) : null
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Delivery updated successfully!');
            location.reload();
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred');
    });
}

// =============================================
// STAFF FUNCTIONS
// =============================================

function deleteStaff(staffId) {
    if (confirm('Are you sure you want to delete this staff member?')) {
        fetch('/staff/' + staffId + '/delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Staff deleted successfully!');
                location.reload();
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred');
        });
    }
}

// =============================================
// REPORT FUNCTIONS
// =============================================

async function loadAverageDeliveryTime(staffId) {
    try {
        const response = await fetch('/reports/average-delivery-time/' + staffId);
        const data = await response.json();
        if (data.success) {
            console.log('Average delivery time for staff ' + staffId + ': ' + data.avg_time + ' minutes');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function loadOrdersNotDelivered30() {
    try {
        const response = await fetch('/api/orders-not-delivered-30mins');
        const data = await response.json();
        if (data.success) {
            console.log('Orders not delivered within 30 minutes:', data.data);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function loadStaffMostDeliveries() {
    try {
        const response = await fetch('/api/staff-most-deliveries');
        const data = await response.json();
        if (data.success) {
            console.log('Staff with most deliveries:', data.data);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function loadCustomerHighestOrders() {
    try {
        const response = await fetch('/api/customer-highest-orders');
        const data = await response.json();
        if (data.success) {
            console.log('Customers with highest orders:', data.data);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function loadOrderDeliveryStatus() {
    try {
        const response = await fetch('/api/order-delivery-status');
        const data = await response.json();
        if (data.success) {
            console.log('Order and delivery status:', data.data);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function loadDeliverySummaryByDate() {
    try {
        const response = await fetch('/api/delivery-summary-by-date');
        const data = await response.json();
        if (data.success) {
            console.log('Delivery summary by date:', data.data);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function loadStaffDeliveryCount() {
    try {
        const response = await fetch('/api/staff-delivery-count');
        const data = await response.json();
        if (data.success) {
            console.log('Staff delivery count:', data.data);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// =============================================
// FORM VALIDATION
// =============================================

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePhone(phone) {
    const re = /^[0-9]{10,15}$/;
    return re.test(phone);
}

function validateForm(formElement) {
    const inputs = formElement.querySelectorAll('[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.style.borderColor = '#dc3545';
        } else {
            input.style.borderColor = '#ddd';
        }
    });
    
    return isValid;
}

// =============================================
// TABLE SEARCH AND FILTER
// =============================================

function searchTable(inputId, tableId) {
    const input = document.getElementById(inputId);
    const table = document.getElementById(tableId);
    
    if (!input || !table) return;
    
    const filter = input.value.toUpperCase();
    const rows = table.querySelectorAll('tbody tr');
    
    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        let match = false;
        
        cells.forEach(cell => {
            if (cell.textContent.toUpperCase().indexOf(filter) > -1) {
                match = true;
            }
        });
        
        row.style.display = match ? '' : 'none';
    });
}

// =============================================
// PRINT FUNCTIONALITY
// =============================================

function printTable(tableId) {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    const printWindow = window.open('', '', 'height=400,width=800');
    printWindow.document.write('<html><head><title>Print Report</title>');
    printWindow.document.write('<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/style.css\') }}">');
    printWindow.document.write('</head><body>');
    printWindow.document.write(table.outerHTML);
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();
}

// =============================================
// DATE PICKER UTILITY
// =============================================

function setMinDate(inputId, days) {
    const input = document.getElementById(inputId);
    if (!input) return;
    
    const today = new Date();
    today.setDate(today.getDate() + days);
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    
    input.min = yyyy + '-' + mm + '-' + dd;
}

// =============================================
// TOAST NOTIFICATIONS
// =============================================

function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = 'toast toast-' + type;
    toast.textContent = message;
    toast.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        padding: 15px 20px;
        background: ${type === 'success' ? '#28a745' : type === 'error' ? '#dc3545' : '#17a2b8'};
        color: white;
        border-radius: 5px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        animation: slideIn 0.3s ease-out;
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// =============================================
// EXPORT TO CSV
// =============================================

function exportTableToCSV(tableId, filename = 'export.csv') {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    let csv = [];
    const rows = table.querySelectorAll('tr');
    
    rows.forEach(row => {
        const cells = row.querySelectorAll('td, th');
        const csvRow = [];
        
        cells.forEach(cell => {
            csvRow.push('"' + cell.textContent.trim().replace(/"/g, '""') + '"');
        });
        
        csv.push(csvRow.join(','));
    });
    
    const csvContent = 'data:text/csv;charset=utf-8,' + csv.join('\n');
    const link = document.createElement('a');
    link.setAttribute('href', encodeURI(csvContent));
    link.setAttribute('download', filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// =============================================
// KEYBOARD SHORTCUTS
// =============================================

document.addEventListener('keydown', function(e) {
    // Ctrl+S for saving (can be customized per page)
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault();
        console.log('Save functionality');
    }
    
    // Escape to close modals
    if (e.key === 'Escape') {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            if (modal.style.display === 'block') {
                modal.style.display = 'none';
            }
        });
    }
});
