# Smart Home Service Platform 🏡

A production-style full-stack application connecting customers with certified technicians for home services (AC repair, AC installation, refrigerator repair, washing machine repair, plumbing, electrical work, TV repair, and household services).

---

## 📁 Directory Structure

```text
smart-home-service-platform/
├── backend/            # FastAPI Python Application
│   ├── app/
│   │   ├── api/        # Routers & API endpoints (/auth, /services, /bookings)
│   │   ├── core/       # Security, JWT, config, storage abstractions
│   │   ├── db/         # Session management & SQLAlchemy Base
│   │   ├── models/     # ORM models (User, Service, Category, Address, Booking, BookingStatusHistory)
│   │   ├── schemas/    # Pydantic data validation schemas
│   │   └── services/   # Core domain business logic (Auth, Catalog, Booking)
│   └── tests/          # Pytest test suite
├── frontend/           # React + TypeScript + Vite Web App
│   ├── src/
│   │   ├── components/ # UI layouts, Navigation, BookingModal
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

- **`CUSTOMER`**: Browse service catalog, create delivery addresses, schedule home visits, describe problems, track live booking status, cancel bookings, view personal booking history (Customer-scoped queries).
- **`TECHNICIAN`**: Manage online availability, view assigned job dispatches, and update job progress (`IN_PROGRESS` -> `COMPLETED`).
- **`ADMIN`**: Platform control center, create/update/deactivate catalog services, manage categories, oversight on technician directory & booking dispatches.

---

## 📅 Booking System & State Machine

### Status Lifecycle
`PENDING` ➔ `ASSIGNED` ➔ `ACCEPTED` ➔ `ON_THE_WAY` ➔ `IN_PROGRESS` ➔ `COMPLETED` (or `CANCELLED`)

Strict transition validation ensures terminal states (`COMPLETED`, `CANCELLED`) cannot be modified, and all state changes are logged in `booking_status_history`.

### Customer Booking API Endpoints
- `POST /api/bookings` — Create a new service booking with address, date, time slot, and problem description
- `GET /api/bookings` — List all bookings belonging exclusively to the current customer
- `GET /api/bookings/{id}` — Retrieve detailed booking information (Customer ownership validation)
- `PUT /api/bookings/{id}/cancel` — Cancel an existing booking (`PENDING` or `ASSIGNED` status)

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

Run backend unit & booking integration tests:
```bash
cd backend
python -m pytest
```
Testing covers:
- `test_booking_creation_workflow`
- `test_booking_invalid_service` (404 Not Found)
- `test_booking_invalid_past_date` (400 Bad Request / 422 Unprocessable)
- `test_unauthorized_customer_booking_access` (403 Forbidden customer isolation)
- `test_booking_cancellation_and_status_history`
- `test_strict_invalid_status_transition` (400 Bad Request state machine error)
- All Auth & Catalog test suites