# KI-Agent Good Friend

Backend service for the **Good Friend** application – a system designed to support meaningful interactions and intelligent assistance.

---

## Features

- RESTful API for client communication
- User and session management
- Integration with external services (e.g. AI / database)
- Scalable backend architecture
- Environment-based configuration

---

## Tech Stack

- Python
- Flask (or FastAPI)
- Database (e.g. Cassandra / Astra DB)
- Cloud-ready deployment

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kosmopy/good-friend-backend.git
cd good-friend-backend

### 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows

### 3. Install dependencies
pip install -r requirements.txt

### Configuration

Create a .env file in the root directory:

# Example configuration
PORT=5000
DEBUG=True

# Database
DB_HOST=your_database_host
DB_KEYSPACE=your_keyspace
DB_USERNAME=your_username
DB_PASSWORD=your_password

# API Keys
API_KEY=your_api_key
SECRET_KEY=your_secret_key
