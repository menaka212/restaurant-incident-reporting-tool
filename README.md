# 🍽️ Restaurant Incident Reporting Tool

## 📌 Overview

The Restaurant Incident Reporting Tool is a web-based application built using Django and PostgreSQL to help restaurant staff report operational incidents and enable administrators to monitor, track, and resolve issues across multiple store locations.

---

# ✨ Features

## 🔹 Core Features

- 📝 Incident Reporting
- 📊 Interactive Dashboard
- 🔄 Incident Status Tracking
- 📁 File/Image Upload Support
- 🔍 Search & Filtering
- 🏪 Multi-Store Incident Management
- 🐘 PostgreSQL Database Integration

## 🔹 Additional Features

- 🔐 User Authentication & Login
- 👥 Role-Based User Access
- 📈 Analytics Dashboard with Charts
- 📱 Responsive Bootstrap UI
- 🔔 Toast Notifications
- ☁️ Cloud Deployment using Render

---

# 👥 User Roles

## 🛡️ Admin

- View all incidents
- Create incidents
- Update incidents
- Delete incidents
- Manage stores
- Manage users
- View analytics dashboard
- Access Django Admin Panel

## 👨‍💼 Manager

- Monitor incidents
- View dashboard analytics
- Track store operations
- Review incident reports

## 👷 Staff

- Create incidents
- Upload supporting files/images
- View own incidents
- Track incident status

---

# 🛠️ Tech Stack

## 🔙 Backend

- 🐍 Python
- 🎯 Django

## 🗄️ Database

- 🐘 PostgreSQL
- ☁️ Neon Database

## 🎨 Frontend

- 🌐 HTML5
- 🎨 CSS3
- 🅱️ Bootstrap 5
- 📊 Chart.js

## 🚀 Deployment

- ☁️ Render
- 🐘 Neon PostgreSQL

---

# 🔑 Demo Credentials

## 🛡️ Admin

- Username: `admin`
- Password: `Admin@123`

## 👨‍💼 Manager

- Username: `manager_chennai`
- Password: `Manager@123`

## 👷 Staff

- Username: `staff1`
- Password: `Staff@123`

---

# 📸 Application Screenshots

## 🔐 Login Page

![Login Page](<Screenshot 2026-05-29 110829.png>)

---

## 📊 Dashboard

![Dashboard]Screenshot 2026-05-29 110957.png

---

## 📈 Analytics Dashboard

![Analytics]Screenshot 2026-05-29 111016.png
![alt text](<Screenshot 2026-05-29 111027.png>)

---

## 📝 Create Incident

![Create Incident]Screenshot 2026-05-29 111147.png Screenshot 2026-05-29 111135.png

---

## 👨‍💼 Admin View

![Admin View]Screenshot 2026-05-29 111203.png

---

## 👷 Staff View

![Staff View]Screenshot 2026-05-29 111245.png

---

# 🌐 Live Demo

### 🚀 Deployed Application

```text
https://your-app-name.onrender.com
```

---

# ⚙️ Installation

```bash
git clone https://github.com/menaka212/restaurant-incident-reporting-tool.git

cd restaurant-incident-reporting-tool

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

---

# 🗄️ Database Models

## 🏪 Store

- Name
- City
- Address

## 🚨 Incident

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

# 📊 System Workflow

1️⃣ User logs into the system.

2️⃣ Staff reports an operational incident.

3️⃣ Incident is stored in Neon PostgreSQL Database.

4️⃣ Admin monitors incidents through the dashboard.

5️⃣ Incident status is updated and resolved.

6️⃣ Analytics dashboard displays incident statistics.

---

# 📸 Features Demonstrated

- ✅ Authentication System
- ✅ Role-Based Access Control
- ✅ Multi-Store Support
- ✅ Incident CRUD Operations
- ✅ File Upload Support
- ✅ Dashboard Analytics
- ✅ PostgreSQL Integration
- ✅ Neon Database Connectivity
- ✅ Responsive UI
- ✅ Render Cloud Deployment

---

# 🔮 Future Enhancements

- 🤖 AI-Based Incident Categorization
- 📧 Email Notifications
- 🔔 Real-Time Alerts
- 📈 Advanced Reporting
- 🏪 Store-Specific Permissions
- 📊 Predictive Incident Analytics

---

# 👩‍💻 Developed By

**Menaka Manavalan**

Full Stack Developer | Django Developer

---
⭐ If you found this project useful, feel free to star the repository.