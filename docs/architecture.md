# System Architecture Documentation

## Overview
The Smart Home Service Platform connects home owners with certified service technicians.

```text
+-----------------------+         +-----------------------+
|  React (TS + Vite)    |  <--->  |  FastAPI (Python)     |
|  Frontend Application |  REST   |  Backend Service      |
+-----------------------+         +-----------------------+
                                              |
                                              v
                                  +-----------------------+
                                  |  PostgreSQL Database  |
                                  +-----------------------+
```

## Core Infrastructure
- **Frontend**: SPA built with React 18, TypeScript, Vite, React Router.
- **Backend**: RESTful API powered by FastAPI, SQLAlchemy 2.0 ORM, Pydantic data validation.
- **Database**: PostgreSQL 15 containerized via Docker Compose.
- **Environment**: Configured using environment variables via `.env.example`.
