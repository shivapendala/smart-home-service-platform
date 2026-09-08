# Smart Home Service Platform 🏡

A production-style full-stack application connecting customers with certified technicians for home services (AC repair, AC installation, refrigerator repair, washing machine repair, plumbing, electrical work, TV repair, and household services).

---

## 🌟 Features

- **Multi-Role User Authentication**: Role-Based Access Control (`CUSTOMER`, `TECHNICIAN`, `ADMIN`) with direct bcrypt password hashing and JWT token authorization.
- **Dynamic Service Catalog**: Directory of home services with upfront pricing, estimated durations, categories, and keyword search.
- **Customer Booking System**: 7-step booking lifecycle (`PENDING` ➔ `ASSIGNED` ➔ `ACCEPTED` ➔ `ON_THE_WAY` ➔ `IN_PROGRESS` ➔ `COMPLETED` / `CANCELLED`), address management, and status audit history.
- **Technician Job Workflow**: Availability toggling, dispatch queues, job state controls, diagnostic notes, and safe before/after photo uploads with file type & size validation.
- **Admin Oversight Center**: Real-time KPI dashboard (Customers, Technicians, Today's Bookings, Pending, Active, Completed, Cancelled, Revenue Summary), directory controls, manual dispatch overrides, refund processing, and complaint resolution ticketing.
- **Payments Abstraction**: Pluggable `PaymentProvider` interface with `MockPaymentProvider` (no hardcoded production secrets).
- **In-App Notification Engine**: Event dispatcher triggering real-time notifications for booking updates, dispatches, job progress, payment receipts, and complaint status changes.
- **Comprehensive E2E & Unit Test Coverage**: 35 Pytest integration tests & Playwright E2E customer-to-review workflow tests.

---

## 🏗️ System Architecture

```text
               +----------------------------------+
               |        React 18 Frontend         |
               | (TypeScript + Vite + Glassmorphism|
               +----------------+-----------------+
                                | HTTP REST APIs (JWT)
                                v
               +----------------+-----------------+
               |         FastAPI Backend          |
               | (Python 3.11+ / SQLAlchemy 2.0)  |
               +-------+------------------+-------+
                       |                  |
                       v                  v
             +---------+------+   +-------+---------+
             | PostgreSQL 15  |   | Local Storage / |
             | Database Container| | S3 Photo Uploads|
             +----------------+   +-----------------+
```

---

## 📁 Project Structure

```text
smart-home-service-platform/
├── backend/            # FastAPI Python Application
│   ├── app/
│   │   ├── api/        # REST Routers (/auth, /services, /bookings, /technicians, /admin, /notifications)
│   │   ├── core/       # Security, JWT, config, storage & payment abstractions, structured logging
│   │   ├── db/         # Session management & SQLAlchemy Base
│   │   ├── models/     # ORM models (User, Service, Category, Address, Booking, TechnicianProfile, Payment, Review, Complaint, Notification)
│   │   ├── schemas/    # Pydantic data validation schemas
│   │   └── services/   # Business domain services
│   ├── tests/          # Pytest test suite (35 passing unit & integration tests)
│   └── Dockerfile
├── frontend/           # React + TypeScript + Vite Web App
│   ├── src/
│   │   ├── components/ # Responsive UI components & modals
│   │   ├── context/    # Global AuthContext & state
│   │   ├── pages/      # Home, Catalog, Auth, Dashboards
│   │   └── services/   # Axios API client
│   ├── e2e/            # Playwright End-to-End test suite
│   ├── Dockerfile
│   ├── nginx.conf
│   └── package.json
├── database/           # PostgreSQL initialization scripts (`init.sql`)
├── docs/               # System architecture & API documentation
├── tests/              # Root integration & health check tests
├── .env.example        # Environment configuration template
├── .gitignore          # Git exclusion rules
├── README.md           # Master project documentation
└── docker-compose.yml  # Multi-container Docker Compose orchestration
```

---

## ⚙️ Environment Configuration

Copy `.env.example` to `.env` before running:

```env
# Backend Configuration
PROJECT_NAME="Smart Home Service Platform"
API_V1_STR="/api/v1"
SECRET_KEY="SUPER_SECRET_KEY_CHANGE_IN_PRODUCTION_9876543210_SMART_HOME"
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Database Configuration
DATABASE_URL="postgresql://postgres:postgrespassword@localhost:5432/smarthome_db"

# Storage Configuration
STORAGE_TYPE="local"
LOCAL_STORAGE_DIR="./uploads"

# CORS Configuration
BACKEND_CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000", "http://localhost:8000"]
```

---

## 🚀 Installation & Local Setup

### 1. Backend Setup
```bash
cd backend
python -m venv venv

# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```
Interactive API docs available at [http://localhost:8000/docs](http://localhost:8000/docs).

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend Web App available at [http://localhost:5173](http://localhost:5173).

---

## 🐳 Docker Deployment

Orchestrate PostgreSQL 15, FastAPI Backend, and React Frontend Nginx containers with Docker Compose:

```bash
docker-compose up --build
```
- **Web Application**: [http://localhost:5173](http://localhost:5173) or [http://localhost](http://localhost)
- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **PostgreSQL Database**: Port `5432`

---

## 🧪 Testing Instructions

### 1. Pytest Backend Integration Tests
```bash
cd backend
python -m pytest
```
- **Total Tests**: 35 passed (0 failed)
- **Coverage**: Authentication, Authorization, Services, Customers, Technicians, Bookings, Status transitions, Payments, Reviews, Complaints, Notifications, Storage.

### 2. Frontend Production Build Verification
```bash
cd frontend
npm run build
```
- **Build Result**: Built cleanly in 3.35s with 0 errors.

### 3. Playwright E2E End-to-End Workflow Tests
```bash
cd frontend
npx playwright test
```
- **Workflow Tested**: Customer Registration/Login ➔ Service Selection ➔ Booking Creation ➔ Admin Technician Assignment ➔ Technician Login & Job Execution (`ACCEPT` ➔ `ON_THE_WAY` ➔ `START` ➔ `COMPLETE`) ➔ Customer Service Review.
- **E2E Result**: 1 passed (0 failed).

---

## 🔒 Security Architecture Notes

1. **Password Hashing**: Plaintext passwords are never stored. Direct `bcrypt` hashing with salt protection.
2. **Secrets & Credentials**: Zero API keys, passwords, or tokens hardcoded in Git. All secrets loaded dynamically via `pydantic-settings`.
3. **Authorization Isolation**: Strict ownership checks on Bookings, Notifications, Reviews, and Technician Dispatches prevent cross-user data leaks (`403 Forbidden`).
4. **File Upload Security**: Uploaded before/after photos validated against allowed extension (`.jpg`, `.jpeg`, `.png`, `.webp`) and MIME types with a strict 5MB size limit and UUID filename sanitization.
5. **SQL Injection & XSS Protection**: SQLAlchemy parameterized query bindings prevent SQL injection; React DOM escaping and Pydantic input sanitization prevent XSS attacks.