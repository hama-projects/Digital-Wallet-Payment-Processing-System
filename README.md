# Digital Wallet & Payment Processing System

A backend FinTech simulation system that models core digital wallet operations, payment processing workflows, fraud detection logic, and reward mechanisms.

The project is built using a modular backend architecture to demonstrate real-world system design principles used in financial applications.

---

## Overview

This system simulates a simplified digital payment platform with the following capabilities:

- User authentication and account management
- Wallet creation and balance handling
- Secure transaction processing
- Fraud detection (rule-based logic)
- Rewards system for user activity
- Admin analytics for monitoring system behavior

The goal of this project is to understand how backend FinTech systems are structured and how different services interact in a scalable architecture.

---

## System Architecture

The backend follows a layered modular architecture:

### API Layer (`api/`)
Handles all HTTP requests using FastAPI:
- Authentication routes
- Wallet operations
- Transaction processing
- Rewards system endpoints
- Admin operations

---

### Service Layer (`services/`)
Contains core business logic:
- Authentication service
- Wallet service
- Payment processor
- Fraud detection engine
- Rewards engine

---

### Models Layer (`models/`)
Defines system entities:
- User
- Wallet
- Transaction
- Rewards

---

### Database Layer (`database/`)
Handles:
- Database connection
- Schema management
- Migration scripts

---

### Analytics Layer (`analytics/`)
Provides:
- Transaction metrics
- System performance data
- Dashboard analytics

---

## Core Features

### User System
- User registration and authentication
- Secure login system

### Wallet System
- Wallet creation per user
- Balance management
- Transaction history tracking

### Payment Processing
- Wallet-to-wallet transfers
- Balance validation
- Transaction status tracking

### Fraud Detection (Prototype)
- Rule-based anomaly detection
- Suspicious transaction flagging
- Risk scoring (basic logic)

### Rewards System
- User reward points
- Transaction-based incentives

### Admin Dashboard
- System overview
- User monitoring
- Transaction analytics

---

## Tech Stack

**Backend**
- FastAPI (Python)
- RESTful API design

**Database**
- PostgreSQL

**Architecture**
- Layered backend design
- Service-oriented structure

**Future Enhancements**
- Machine Learning (fraud detection)
- Event-driven architecture
- Real-time transaction processing

---

## Project Structure

```text id="fintech_structure"
backend/
│
├── api/
├── services/
├── models/
├── database/
├── analytics/
│
├── main.py
├── config.py
```

---

## API Documentation

Once the server is running, access API docs:

http://127.0.0.1:8000/docs

---

## Setup Instructions

### Install dependencies
```bash id="setup1"
pip install -r requirements.txt
```

### Run database migrations
```bash id="setup2"
# run migrations.sql in PostgreSQL
```

### Start server
```bash id="setup3"
uvicorn backend.main:app --reload
```

---

## Learning Outcomes

This project demonstrates:

- Backend system design
- REST API development
- Financial transaction workflows
- Modular architecture (service-based design)
- Basic fraud detection logic
- Analytics integration

---

## Important Note

This project is a **FinTech simulation system built for learning and portfolio purposes**.  
It is not intended for real financial transactions.

---

## Author

Moiz Ahmed  
BS Computer Science – Virtual University of Pakistan
