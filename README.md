# Smart Home Service Platform 🏡

A production-style full-stack application connecting customers with certified technicians for home services (AC repair, refrigerator repair, washing machine repair, plumbing, electrical work, and household services).

---

## 📁 Directory Structure

```text
smart-home-service-platform/
├── backend/            # FastAPI Python Application
│   ├── app/
│   │   ├── api/        # Routers & API endpoints (/auth, /services, /bookings)
│   │   ├── core/       # Security, JWT, config, storage abstractions
│   │   ├── db/         # Session management & SQLAlchemy Base
│   │   ├── models/     # ORM models (User, UserRole, Service, Booking)
│   │   ├── schemas/    # Pydantic data validation schemas
│   │   └── services/   # Core domain business logic
│   └── tests/          # Pytest test suite (Auth, Services, Bookings, Storage)
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

## 🔐 User Roles & Authentication Architecture

The platform supports 3 primary user roles:
- **`CUSTOMER`**: Can browse service catalog, schedule home visits, track live booking progress, and view receipts.
- **`TECHNICIAN`**: Can toggle online availability, view assigned job dispatches, and update job progress (`IN_PROGRESS` -> `COMPLETED`).
- **`ADMIN`**: Full platform control center, service catalog CRUD management, technician directory oversight, and manual booking assignment overrides.

### Authentication API Endpoints
- `POST /api/auth/register` — Register a new user (`CUSTOMER`, `TECHNICIAN`, or `ADMIN`)
- `POST /api/auth/login` — Authenticate credentials & receive JWT bearer token
- `GET /api/auth/me` — Retrieve profile details for current authenticated user

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

Run backend unit and role-authorization integration tests:
```bash
cd backend
python -m pytest
```
Testing covers:
- `test_user_registration_customer`
- `test_user_registration_technician`
- `test_user_registration_duplicate_email`
- `test_user_login`
- `test_user_login_invalid_password`
- `test_invalid_token`
- `test_get_current_user_profile`
- `test_unauthorized_profile_access`
- `test_role_authorization_admin_only`
- `test_direct_api_auth_routes`