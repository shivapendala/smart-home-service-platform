# Smart Home Service Platform 🏡

A production-style full-stack application connecting customers with certified technicians for home services (AC repair, AC installation, refrigerator repair, washing machine repair, plumbing, electrical work, TV repair, and household services).

---

## 📁 Directory Structure

```text
smart-home-service-platform/
├── backend/            # FastAPI Python Application
│   ├── app/
│   │   ├── api/        # Routers & API endpoints (/auth, /services, /bookings, /technicians)
│   │   ├── core/       # Security, JWT, config, storage abstractions
│   │   ├── db/         # Session management & SQLAlchemy Base
│   │   ├── models/     # ORM models (User, Service, Category, Address, Booking, TechnicianProfile, ServicePhoto, ServiceNote)
│   │   ├── schemas/    # Pydantic data validation schemas
│   │   └── services/   # Core domain business logic (Auth, Catalog, Booking, Technician)
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

- **`CUSTOMER`**: Browse service catalog, create delivery addresses, schedule home visits, describe problems, track live booking status, cancel bookings, view personal booking history.
- **`TECHNICIAN`**: Toggle online availability, view assigned job dispatches (New Assigned, Today's Jobs, Active Job, Completed Jobs), execute workflow status actions, write diagnostic notes, and upload before/after photos with file security validation. (Strict security isolation: Technicians may only access bookings assigned to them).
- **`ADMIN`**: Platform control center, create/update/deactivate catalog services, manage categories, oversight on technician directory & dispatch assignments.

---

## 🔧 Technician Job Workflow & File Security

### Job State Transitions
`ASSIGNED` ➔ `ACCEPTED` ➔ `ON_THE_WAY` ➔ `IN_PROGRESS` ➔ `COMPLETED`
(Or `REJECT` ➔ returns job to `PENDING` queue for re-assignment).

### Safe Local File Upload Validation
- **Supported File Types**: JPG, JPEG, PNG, WEBP (`ALLOWED_MIME_TYPES = image/jpeg, image/png, image/webp`).
- **File Size Limit**: Strict 5MB ceiling per photo.
- **Sanitization & Storage**: Filenames sanitized with UUIDs and saved via `LocalStorageProvider` abstraction.
- **Authorization Enforcement**: Uploads restricted to assigned technician or booking owner customer (`403 Forbidden` on unauthorized attempts).

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

Run backend unit & technician workflow integration tests:
```bash
cd backend
python -m pytest
```
Testing covers:
- `test_technician_complete_workflow` (`ASSIGNED` ➔ `ACCEPTED` ➔ `ON_THE_WAY` ➔ `IN_PROGRESS` ➔ `COMPLETED`)
- `test_technician_job_rejection`
- `test_unrelated_technician_security_isolation` (403 Forbidden on unauthorized job access)
- `test_photo_upload_and_validation` (Valid JPEG upload & invalid `.txt` rejection)
- `test_service_notes`
- All Auth, Catalog, Booking, and Storage test suites (29 passing tests)