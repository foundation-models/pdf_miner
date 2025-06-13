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


# Extraction via ChatGPT

You can use this prompt to perform such an extraction
```
I’m uploading a PDF file. Please extract all readable content from each page — including OCR from image-based or scanned pages — and output it as a JSON array.

Each item in the array should have the following structure:

{
  "page": <page_number>,
  "content": "<full text content from that page>",
  "URL": "<base_pdf_url>#page=<page_number>"
}

Use this base PDF URL: https://www.deltadentalar.com/docs/default-source/providers/2025-dentist-handbook.pdf

Make sure no visible content is skipped. Extract text from images using OCR if necessary. Remove repeated headers/footers (like “Dentist Handbook January 2025” or “Page | X”) unless they're part of meaningful content. Return the full JSON or a downloadable file if large.
```

## Authentication

This service uses OAuth 2.0 with Client Credentials flow for authentication. Make sure to configure your client credentials before making authenticated requests.
