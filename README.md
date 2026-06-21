# Digital Wallet & Payment Processing System

A backend FinTech simulation system that models core digital wallet operations, payment processing, fraud detection, rewards management, and system analytics.

The project is designed to demonstrate real-world backend system design using a modular, service-based architecture.

---

## Overview

This system simulates a simplified financial platform with the following capabilities:

- User authentication and account management
- Wallet creation and balance handling
- Secure payment processing between users
- Rule-based fraud detection
- Rewards system based on user activity
- Admin-level analytics and monitoring

---

## System Architecture

The system follows a layered backend architecture:

Client → API Layer → Service Layer → Database → Response

### API Layer
Handles incoming HTTP requests using FastAPI:
- Authentication routes
- Wallet routes
- Transaction routes
- Rewards routes
- Admin routes

---

### Service Layer
Contains all business logic:

- Authentication service
- Wallet management service
- Payment processing engine
- Fraud detection rules engine
- Rewards calculation engine

---

### Database Layer
PostgreSQL-based storage system for:

- Users
- Wallets
- Transactions
- Rewards

---

### Analytics Layer
Provides system insights:

- Transaction metrics
- User activity tracking
- Admin dashboard statistics

---

## Core Features

### Authentication System
- User registration and login
- JWT-based authentication

### Wallet System
- Wallet creation
- Deposit functionality
- Balance tracking

### Transaction System
- Peer-to-peer payments
- Transaction history logging
- Balance validation

### Fraud Detection
- Rule-based fraud detection
- Transaction threshold monitoring
- Suspicious activity flagging

### Rewards System
- Points calculation based on transactions
- User engagement tracking

### Admin Dashboard
- System-wide statistics
- User and transaction monitoring

---

## API Endpoints

Base URL:
http://localhost:8000

### Authentication
- POST /auth/register
- POST /auth/login

### Wallet
- POST /wallet/deposit
- GET /wallet/{user_id}

### Transactions
- POST /transactions/send

### Rewards
- GET /rewards/{user_id}

### Admin
- GET /admin/dashboard

---

## Project Structure

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

---

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- REST API architecture
- Modular backend design

---

## Future Improvements

- Machine learning-based fraud detection
- Risk scoring system
- Real-time transaction processing
- Event-driven architecture
- Docker containerization
- Scalable microservice migration

---

## Note

This project is a FinTech simulation built for learning and portfolio purposes. It does not represent a production-level financial system.

---

## Author

Moiz Ahmed  
BS Computer Science – Virtual University of Pakistan
