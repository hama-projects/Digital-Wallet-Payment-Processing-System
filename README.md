# Digital Wallet & Payment Processing System

A backend FinTech simulation system that demonstrates core digital wallet operations, secure transactions, fraud detection logic, rewards processing, and system analytics using a modular service-based architecture.

---

## Overview

This project simulates a simplified financial system where users can:

- Register and authenticate securely
- Manage digital wallets
- Send and receive payments
- Track transaction history
- Earn reward points
- View system analytics through admin dashboard

The goal is to demonstrate backend system design, API development, and financial workflow implementation.

---

## System Architecture

The system follows a layered backend architecture:

```
Client (Frontend - optional)
        ↓
API Layer (FastAPI)
        ↓
Service Layer (Business Logic)
        ↓
Database Layer (PostgreSQL)
```

### API Layer
Handles:
- Routing
- Input validation
- Authentication (JWT)

### Service Layer
Handles business logic:
- Wallet operations
- Payment processing
- Fraud detection rules
- Rewards calculation

### Database Layer
Stores:
- Users
- Wallets
- Transactions
- Rewards

---

## Core Modules

### Authentication Module
- User registration
- Login system
- JWT authentication

### Wallet Module
- Wallet creation
- Deposit funds
- Balance tracking

### Transaction Module
- Peer-to-peer transfers
- Transaction history logging

### Fraud Detection Module
- Rule-based fraud detection
- Transaction threshold monitoring

### Rewards Module
- Points calculation based on activity

### Analytics Module
- Transaction statistics
- System usage metrics
- Admin dashboard data

---

## API Endpoints

**Base URL**
```
http://localhost:8000
```

### Authentication
- POST `/auth/register`
- POST `/auth/login`

### Wallet
- POST `/wallet/deposit`
- GET `/wallet/{user_id}`

### Transactions
- POST `/transactions/send`

### Rewards
- GET `/rewards/{user_id}`

### Admin
- GET `/admin/dashboard`

---

## Project Structure

```
backend/
├── api/
├── services/
├── models/
├── database/
├── analytics/
├── config.py
├── main.py

tests/
├── __init__.py

docs.md
requirements.md
```

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- REST API architecture
- Modular backend design

---

## Key Features

- Secure authentication system (JWT)
- Wallet-based transaction system
- Rule-based fraud detection
- Rewards and analytics system
- Modular service-based architecture

---

## Future Improvements

- Machine learning-based fraud detection
- Risk scoring system
- Real-time transaction processing
- Event-driven architecture
- Docker containerization
- Cloud deployment (AWS / Azure)

---

## Note

This project is a FinTech simulation built for learning and portfolio purposes. It does not process real financial transactions.

---

## Author

Moiz Ahmed  
BS Computer Science – Virtual University of Pakistan
