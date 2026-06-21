CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE wallets (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    balance NUMERIC DEFAULT 0
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    sender_id INTEGER,
    receiver_id INTEGER,
    amount NUMERIC,
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rewards (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    points INTEGER DEFAULT 0
);