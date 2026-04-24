# Truth Guard 🛡️

Truth Guard is a machine learning-powered web application that detects Fake News. It features a modern, ChatGPT-like chatbot interface where users can paste news articles to get a real-time prediction (Real vs. Fake) along with a confidence score.

## Features
- **Machine Learning**: Uses TF-IDF Vectorization and Logistic Regression to analyze text.
- **Backend API**: Powered by FastAPI for lightning-fast inference and predictions.
- **Chatbot UI**: A beautiful, responsive, and animated chat interface built with HTML, CSS, and Vanilla JavaScript.

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train the machine learning model:
   ```bash
   python train_model.py
   ```
3. Run the backend server:
   ```bash
   python -m uvicorn app:app --reload
   ```
4. Open your browser and navigate to `http://127.0.0.1:8000` to chat with Truth Guard!
