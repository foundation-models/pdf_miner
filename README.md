# PDF Miner Service

A service for extracting and processing text from PDF documents.

## Prerequisites

- Python 3.12
- `uv` package manager
- `make` utility

## Setup and Installation

1. Create and activate a virtual environment:
   ```bash
   uv venv --python 3.12
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

## Running the Service

To start the web application:

```bash
make run-web-app
```

## API Documentation

Once the service is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Authentication

This service uses OAuth 2.0 with Client Credentials flow for authentication. Make sure to configure your client credentials before making authenticated requests.
