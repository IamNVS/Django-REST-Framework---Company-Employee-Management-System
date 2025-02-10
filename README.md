# Django-REST-Framework---Company-Employee-Management-System
A Django REST Framework project to manage company and employee records with a one-to-many relationship (Company → Employees). It supports full CRUD operations, an admin panel for managing records, and search functionality by employee name. SQLite is used as the database.

# **Company & Employee Management System (Django REST Framework)**  

## **Overview**  
The **Company & Employee Management System** is a **Django REST Framework (DRF)** based project that provides an API to manage **companies and employees** with a **one-to-many relationship** (one company can have multiple employees).  

This system allows **full CRUD (Create, Read, Update, Delete) operations** for companies and employees, making it easy to **add, modify, delete, and retrieve** records via API endpoints. Additionally, it features an **admin panel**, where administrators can manage companies and employees, including the ability to **search employees by name**.  

The database used is **SQLite**, ensuring lightweight and efficient storage.  

---

## **Key Features**  

✅ **One-to-Many Relationship (Company → Employees)**  
✅ **Full CRUD Operations for Companies & Employees**  
✅ **RESTful API with Django REST Framework**  
✅ **Django Admin Panel for Management**  
✅ **Search Employees by Name**  
✅ **Lightweight SQLite Database**  
✅ **Secure and Scalable**  

## **Technologies Used**  

🚀 **Backend:** Django REST Framework (DRF)  
💾 **Database:** SQLite  
🛠️ **Admin Panel:** Django Admin  
🔍 **Search:** Django ORM Queries  
🔗 **API Development:** RESTful APIs  

---

## **API Endpoints**  

This project provides a **RESTful API** to perform operations on **companies** and **employees**.

### **Company Endpoints**  
| Method | Endpoint               | Description              |
|--------|------------------------|--------------------------|
| GET    | `/api/companies/`       | Retrieve all companies  |
| POST   | `/api/companies/`       | Create a new company   |
| GET    | `/api/companies/{id}/`  | Retrieve a specific company |
| PUT    | `/api/companies/{id}/`  | Update a company |
| DELETE | `/api/companies/{id}/`  | Delete a company |

### **Employee Endpoints**  
| Method | Endpoint               | Description              |
|--------|------------------------|--------------------------|
| GET    | `/api/employees/`       | Retrieve all employees  |
| POST   | `/api/employees/`       | Create a new employee   |
| GET    | `/api/employees/{id}/`  | Retrieve a specific employee |
| PUT    | `/api/employees/{id}/`  | Update an employee |
| DELETE | `/api/employees/{id}/`  | Delete an employee |

### **Search Employee by Name**  
To search for employees by name, use:  
```sh
GET /api/employees/?search=<employee_name>

