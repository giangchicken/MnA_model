# M&A Detection API with FastAPI and Docker

## Overview

This project provides an API for detecting Mergers & Acquisitions (M&A) based on HTML news data. The model is served using FastAPI and packaged into a Docker container for easy deployment.

## Prerequisites

- Docker installed on your system.

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Step 2: Build the Docker Image

```bash
docker build -t mna-detection .
```

### Step 3: Run the Container

```bash
docker run -p 8000:8000 mna-detection
```

### Step 4: Access the API

Once the container is running, the API will be accessible at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

### 1. Health Check

**Endpoint:** `GET /health`

**Description:** Checks if the API is running.

**Response:**

```json
{"status": "ok"}
```

### 2. Predict M&A Detection

**Endpoint:** `POST /predict`

**Description:** Processes HTML files and predicts M&A-related content.

**Request Body:**

```json
{
  "folder": "path/to/html/files",
  "threshold": 0.2
}
```

**Response:**

```json
[
  {
    "file": "example.html",
    "prediction": "M&A detected",
    "score": 0.85
  }
]
```

## Requirements File (requirements.txt)

```
fastapi
uvicorn
tqdm
h2o
sentence-transformers
numpy
pandas
scikit-learn
argparse
sentence_transformers
newspaper4k
```

## Notes

- Ensure the necessary folders and models are available within the container.
- Modify `api.py` as needed to fit additional requirements.
- Logs can be viewed inside the container using:
  ```bash
  docker logs <container-id>
  ```

