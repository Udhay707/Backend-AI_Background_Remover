# Background Removal App (Backend with Flask)

This project provides an API for removing the background of images using AI-based models. The backend is built with Flask, and it allows users to upload images, process them, and return the image with the background removed.

## Features

- **POST `/remove-bg`**: Upload an image and get the background removed.
  
## Requirements

- Python 3.8+
- Flask
- ONNX Runtime (for running models)
  
## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/Udhay707/Backend-AI_Background_Remover.git
cd Backend-AI_Background_Remover

###2. Create a virtual environment:
```bash
python3 -m venv venv
###3. Activate the virtual environment:
For Linux/macOS:

```bash
source venv/bin/activate
For Windows:

```bash
venv\Scripts\activate

###4. Install dependencies:
```bash
pip install -r requirements.txt

###5. Run the Flask app:
```bash
python app.py
The server will be running at http://127.0.0.1:5000/.

###6. Test the API with Postman or any HTTP client:
POST /remove-bg to upload an image and get the processed image (background removed).
Usage
Endpoint: /remove-bg

Method: POST

Request:

You need to send an image file (JPEG, PNG) in the request body.
Example request in Postman:
URL: http://127.0.0.1:5000/remove-bg
Method: POST
Body: form-data, with key image and value set to the image file.
Response:

The response will contain the processed image as a base64-encoded string.
Example:
json
Copy code
{
    "image": "iVBORw0KGgoAAAANS..."
}
You can convert this base64 string back to an image using Postman or by decoding it programmatically.

Contributions
Feel free to fork the repo and submit pull requests. Any improvements, features, or bug fixes are welcome!

Guidelines for contributing:
Fork the repository.
Clone your fork to your local machine.
Create a new branch: git checkout -b feature-branch.
Commit your changes: git commit -m 'Add new feature'.
Push to the branch: git push origin feature-branch.
Create a pull request.

