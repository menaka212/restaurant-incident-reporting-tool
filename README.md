## 🍽️ Restaurant Incident Reporting Tool

### 📌 Overview

The Restaurant Incident Reporting Tool is a web-based application designed to help restaurant staff report operational incidents and enable managers/admins to track, monitor, and resolve issues across multiple store locations.

---

## ✨ Features

### 🔹 Core Features

- 📝 Incident Reporting
- 📊 Incident Dashboard
- 🔄 Incident Status Management
- 📁 File/Image Upload
- 🔍 Search & Filtering
- 🐘 PostgreSQL Database

### 🔹 Bonus Features

- 🔐 Authentication & Login
- 👥 Role-Based Access Control
- 🏪 Multi-Store Support
- 📱 Responsive UI
- 📈 Analytics Dashboard
- 🔔 Toast Notifications

---

## 👨‍💼 User Roles

### 🛡️ Admin
- View all incidents
- Update incidents
- Delete incidents
- Manage stores
- Manage users

### 👨‍💻 Manager
- Monitor incidents
- View dashboard analytics
- Track store operations

### 👷 Staff
- Create incidents
- View own incidents
- Upload supporting files

---

## 🛠️ Tech Stack

### 🔙 Backend

- 🐍 Python
- 🎯 Django
- 🐘 PostgreSQL

### 🎨 Frontend

- 🌐 HTML5
- 🎨 CSS3
- 🅱️ Bootstrap 5
- 📊 Chart.js

### ☁️ Deployment

- 🚀 Render

## 🔑 Demo Credentials

### 🛡️ Admin
- Username: admin
- Password: Admin@123

### 👨‍💼 Manager
- Username: manager_chennai
- Password: Manager@123

### 👷 Staff
- Username: staff_kfc
- Password: Staff@123

---

## 📸 Application Screenshots

### 🔐 Login Page

![Login Page](<Screenshot 2026-05-29 110829.png>)

---

### 📊 Dashboard

![Dashboard](<Screenshot 2026-05-29 110957.png>)

---

### 📈 Analytics Dashboard

![Analytics](<Screenshot 2026-05-29 111016.png>)
![Incidents](<Screenshot 2026-05-29 111027.png>)
---

### 📝 Create Incident

![Create Incident](<Screenshot 2026-05-29 111135.png>)
![Submission](<Screenshot 2026-05-29 111147.png>)

---

### 👨‍💼 Admin View

![Admin View](<Screenshot 2026-05-29 111203.png>)
---

### 👷 Staff View

![Staff View](<Screenshot 2026-05-29 111245.png>)

---

## 🚀 Installation
git clone https://github.com/menaka212/restaurant-incident-reporting-tool
cd restaurant-incident-tool

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

---

## 🗄️ Database Models

### 🏪 Store
- Store Name
- City
- Address

### 🚨 Incident
- Title
- Description
- Category
- Severity
- Status
- Attachment
- Store
- Created By
- Created At

---

## 📊 System Workflow

- 1️⃣ Staff logs in and reports an incident.
- 2️⃣ Incident is stored in PostgreSQL database.
- 3️⃣ Managers/Admins monitor incidents through   the dashboard.
- 4️⃣ Admin updates status and resolves issues.
- 5️⃣ Analytics dashboard displays incident statistics.

---

## 📸 Features Demonstrated

- ✅ Authentication System
- ✅ Role-Based Access Control
- ✅ Multi-Store Management
- ✅ Incident CRUD Operations
- ✅ File Upload Support
- ✅ Dashboard Analytics
- ✅ Responsive Design
- ✅ PostgreSQL Integration
- ✅ Render Deployment Ready

---

## 🔮 Future Enhancements

- 🤖 AI-Powered Incident Categorization
- 📧 Email Notifications
- 🔔 Real-Time Alerts
- 🏬 Store-Specific Manager Permissions
- 📈 Advanced Analytics & Reporting

---