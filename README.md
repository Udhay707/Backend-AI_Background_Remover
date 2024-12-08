# Background Removal App (Backend with Flask)

This project provides an API for removing the background of images using AI-based models. The backend is built with Flask, and it allows users to upload images, process them, and return the image with the background removed.

## Features

- **POST `/remove-bg`**: Upload an image and get the background removed.
  
## Requirements

- Python 3.8+
- Flask
- ONNX Runtime (for running models)
  
## Build Project

### 1. Clone the repository:

```bash
git clone https://github.com/Udhay707/Backend-AI_Background_Remover.git
cd Backend-AI_Background_Remover
```

### 2. Create a virtual environment:
```bash
python3 -m venv venv
###3. Activate the virtual environment:
For Linux/macOS:
```
```bash
source venv/bin/activate
For Windows:
```
```bash
venv\Scripts\activate
```
### 4. Install dependencies:
```bash
pip install -r requirements.txt
```
### 5. Run the Flask app:
```bash
python app.py
The server will be running at http://127.0.0.1:5000/.
```
## Build Docker Image
### 1. Build Image
```bash
docker build -t backend-ai-bg-remover .
```
### 2. Create a container and execute
```bash
docker run -d -p 5000:5000 --name backend-bg-remover-container backend-ai-bg-remover
```

## Execute docker image from Repo
### 1. Pull image
```bash
docker pull udhay707/backend-ai-bg-remover
```
### 2. Create a container and execute
```bash
docker run -d -p 5000:5000 --name backend-bg-remove-container udhay707/backend-ai-bg-remover
```
