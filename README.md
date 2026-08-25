# Smart Home Service Platform 🏡

A production-style full-stack application connecting customers with certified technicians for home services (AC repair, AC installation, refrigerator repair, washing machine repair, plumbing, electrical work, TV repair, and household services).

---

## 📁 Directory Structure

```text
smart-home-service-platform/
├── backend/            # FastAPI Python Application
│   ├── app/
│   │   ├── api/        # Routers & API endpoints (/auth, /services, /bookings, /technicians, /admin)
│   │   ├── core/       # Security, JWT, config, storage & payment abstractions
│   │   ├── db/         # Session management & SQLAlchemy Base
│   │   ├── models/     # ORM models (User, Service, Category, Address, Booking, TechnicianProfile, Payment, Review, Complaint)
│   │   ├── schemas/    # Pydantic data validation schemas
│   │   └── services/   # Core domain business logic (Auth, Catalog, Booking, Technician, Admin)
│   └── tests/          # Pytest test suite
├── frontend/           # React + TypeScript + Vite Web App
│   ├── src/
│   │   ├── components/ # UI layouts, Navigation, Modals
│   │   ├── context/    # AuthContext & global state management
│   │   ├── pages/      # Home, Service Catalog, Login, Register & Dashboards
│   │   ├── services/   # Axios API client
│   │   └── types/      # TypeScript interfaces
│   ├── Dockerfile
│   ├── nginx.conf
│   └── package.json
├── database/           # PostgreSQL initialization scripts
├── docs/               # Architecture & API documentation
├── tests/              # Root integration test suite
├── .env.example        # Environment variables template
├── .gitignore          # Git exclusion rules
├── README.md           # Project documentation
└── docker-compose.yml  # Docker orchestration configuration
```

---

## 🔐 User Roles & Scoped Workflows

- **`CUSTOMER`**: Browse catalog, schedule visits, track live progress, make payments, submit 1-5 star reviews (on `COMPLETED` jobs), file complaints, cancel bookings.
- **`TECHNICIAN`**: Toggle availability, manage dispatch queues (`ASSIGNED` ➔ `ACCEPTED` ➔ `ON_THE_WAY` ➔ `IN_PROGRESS` ➔ `COMPLETED`), attach diagnostic notes, upload before/after photos with file security validation.
- **`ADMIN`**: Full platform oversight — Dashboard KPI cards (Total Customers, Technicians, Today's Bookings, Pending, Active, Completed, Cancelled, Revenue Summary), customer/technician directory management, manual booking assignments, payment refund controls, review statistics, and complaint resolution ticketing.

---

## 💳 Payments Abstraction & State Machine

- **Abstraction**: `PaymentProvider` ABC with `MockPaymentProvider` implementation (no real payment secrets in Git).
- **Payment States**: `PENDING` ➔ `PAID` ➔ `REFUNDED` (or `FAILED`).

---

## ⭐️ Reviews & 🎫 Complaints System

- **Reviews**: Allowed only after `COMPLETED` status. Prevents duplicate reviews per booking (`400 Bad Request`).
- **Complaints**: Customers file tickets; Admins assign, update status (`OPEN`, `IN_PROGRESS`, `RESOLVED`, `REJECTED`), and record resolution notes.

---

## 🛠️ Technology Stack

- **Frontend**: React 18, TypeScript, Vite, React Router DOM, Custom Glassmorphism CSS System
- **Backend**: Python 3.11+, FastAPI, SQLAlchemy 2.0 ORM, Pydantic v2, bcrypt password hashing, JWT
- **Database**: PostgreSQL 15 (Docker Compose) / SQLite (Local Dev & Pytest)
- **DevOps & Testing**: Docker, Docker Compose, Nginx, Pytest, Playwright

---

## 🚀 Quick Start & Local Setup

### 1. Environment Setup
```bash
cp .env.example .env
```

### 2. Backend Setup
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

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend runs at [http://localhost:5173](http://localhost:5173).

---

## 🐳 Docker Deployment

To launch all containerized services (PostgreSQL, FastAPI Backend, React Frontend):
```bash
docker-compose up --build
```

---

## 🧪 Testing Suite

Run full backend test suite:
```bash
cd backend
python -m pytest
```
Testing covers:
- `test_admin_dashboard_stats` (KPI calculations & 403 authorization check)
- `test_payment_and_refund_workflow` (Payment creation `PAID`, block duplicate payment, Admin refund `REFUNDED`)
- `test_review_creation_and_duplicate_block` (Completed status enforcement & block duplicate review)
- `test_complaint_ticketing_and_admin_resolution` (Complaint filing & Admin resolution)
- All Auth, Catalog, Booking, Technician, and Storage test suites (33 passing tests)