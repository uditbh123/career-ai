# Backend Architecture

The backend is responsible for all business logic, authentication, AI integrations, database operations, and communication with external services.

The backend follows a layered architecture.

## Request Flow

Client Request

↓

API Layer

↓

Service Layer

↓

Repository Layer

↓

Database

## Layer Responsibilities

### API Layer

Receives HTTP requests and returns HTTP responses.

Responsibilities:

* Validate requests
* Call services
* Return responses

Business logic should never be implemented here.

---

### Service Layer

Contains the application's business logic.

Examples:

* User management
* Resume generation
* Job scoring
* Authentication
* Interview preparation

---

### Repository Layer

Handles communication with the database.

Responsibilities:

* Read data
* Write data
* Update records
* Delete records

Repositories never contain business rules.

---

### Database Layer

Stores persistent application data.

Examples:

* Users
* Profiles
* Jobs
* Applications
* Skills

## Why This Architecture?

Separating responsibilities makes the project easier to test, maintain, and extend.
