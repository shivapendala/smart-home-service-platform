# Smart Home Service Platform 🏡

A production-style full-stack application connecting customers with certified technicians for home services (AC repair, AC installation, refrigerator repair, washing machine repair, plumbing, electrical work, TV repair, and household services).

---

## 📁 Directory Structure

```text
smart-home-service-platform/
├── backend/            # FastAPI Python Application
│   ├── app/
│   │   ├── api/        # Routers & API endpoints (/auth, /services, /bookings, /technicians, /admin, /notifications)
│   │   ├── core/       # Security, JWT, config, storage & payment abstractions
│   │   ├── db/         # Session management & SQLAlchemy Base
│   │   ├── models/     # ORM models (User, Service, Category, Address, Booking, TechnicianProfile, Payment, Review, Complaint, Notification)
│   │   ├── schemas/    # Pydantic data validation schemas
│   │   └── services/   # Core domain business logic (Auth, Catalog, Booking, Technician, Admin, Notification)
│   └── tests/          # Pytest test suite
├── frontend/           # React + TypeScript + Vite Web App
│   ├── src/
│   │   ├── components/ # UI layouts, Navigation, Modals, Notification Bell
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

- **`CUSTOMER`**: Browse catalog, schedule visits, track live progress, make payments, submit 1-5 star reviews (on `COMPLETED` jobs), file complaints, cancel bookings, receive real-time in-app notifications.
- **`TECHNICIAN`**: Toggle availability, manage dispatch queues (`ASSIGNED` ➔ `ACCEPTED` ➔ `ON_THE_WAY` ➔ `IN_PROGRESS` ➔ `COMPLETED`), attach diagnostic notes, upload before/after photos with file security validation, receive job dispatch notifications.
- **`ADMIN`**: Full platform oversight — Dashboard KPI cards (Total Customers, Technicians, Today's Bookings, Pending, Active, Completed, Cancelled, Revenue Summary), customer/technician directory management, manual booking assignments, payment refund controls, review statistics, and complaint resolution ticketing.

---

## 🔔 In-App Notification System & Event Dispatcher

- **Architecture**: `NotificationService` central dispatcher decoupling notification creation from core domain logic. Ready for seamless integration with Email (SMTP/SES) and SMS (Twilio) providers.
- **Automated Event Triggers**:
  - **Booking Created**: Notifies Customer with booking confirmation.
  - **Technician Assigned**: Notifies Customer of assigned technician name & Notifies Technician of new job dispatch.
  - **Job Status Changes**: Notifies Customer when technician Accepts job, marks `ON_THE_WAY`, Starts service, and Completes service.
  - **Payment Completed**: Notifies Customer with transaction confirmation ID.
  - **Complaint Updated**: Notifies Customer when Admin updates complaint status or resolution notes.

### Notification API Endpoints
- `GET /api/notifications` — Fetch user notifications & unread count
- `PATCH /api/notifications/{id}/read` — Mark single notification as read (User isolation check)
- `PATCH /api/notifications/read-all` — Mark all user notifications as read

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
- `test_notification_creation_and_triggers` (Booking creation, technician assignment dispatch, job status transitions)
- `test_mark_as_read_and_security_isolation` (User isolation `403 Forbidden` block & mark read all)
- All Auth, Catalog, Booking, Technician, Admin, Payments, and Storage test suites (35 passing tests)