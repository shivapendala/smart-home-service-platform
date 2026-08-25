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
│   │   ├── models/     # ORM models (User, Service, Category, Booking)
│   │   ├── schemas/    # Pydantic data validation schemas
│   │   └── services/   # Core domain business logic (Auth, Catalog, Booking)
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

## 🔐 User Roles & Authorization

- **`CUSTOMER`**: Browse service catalog, filter by category, search by keyword, view service details, schedule bookings.
- **`TECHNICIAN`**: Manage online availability, view incoming job dispatches, and update job progress (`IN_PROGRESS` -> `COMPLETED`).
- **`ADMIN`**: Platform control center, create/update/deactivate catalog services, manage categories, oversight on technician directory & booking dispatches.

---

## 📋 Service Catalog API Endpoints

- `GET /api/services` — List active services with optional category filtering (`?category_id=X`) & search (`?search=kw`)
- `GET /api/services/{id}` — Retrieve detailed information for a single service item
- `POST /api/services` — Create a new service item (**Admin only**)
- `PUT /api/services/{id}` — Update existing service details & upfront base price (**Admin only**)
- `DELETE /api/services/{id}` — Deactivate or delete a service item (**Admin only**)
- `GET /api/services/categories` — List available service categories (AC Repair, AC Installation, Refrigerator Repair, Washing Machine Repair, Plumbing, Electrical, TV Repair)

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

Run backend unit & service catalog integration tests:
```bash
cd backend
python -m pytest
```
Testing covers:
- `test_list_categories_auto_seeds`
- `test_customer_browsing_and_retrieval`
- `test_search_and_category_filter`
- `test_admin_create_update_and_deactivate_service`
- `test_unauthorized_modification_attempts` (returns 403 Forbidden)
- All Auth & Storage test suites