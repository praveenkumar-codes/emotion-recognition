# Emotion AI Dashboard

A real-time Image-Based Emotion Recognition System built using Deep Learning and Hugging Face pre-trained models.
This project detects human emotions from images and live webcam feeds through a modern web dashboard.

---

## Features

* Real-time Webcam Emotion Detection
* Image Upload and Prediction
* Pre-trained Deep Learning Model (Hugging Face)
* Interactive Web Dashboard using Flask
* Fast and Accurate Predictions
* Clean and Responsive UI

---

## Project Structure

```
emotion_ai_dashboard/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── uploads/
│
├── templates/
│   └── index.html
│
├── app.py
├── model.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/emotion-ai-dashboard.git
cd emotion-ai-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## Model Used

This project uses a pre-trained model from Hugging Face:

* dima806/facial_emotions_image_detection

No training is required. The model is ready for real-time inference.

---

## Emotions Detected

* Happy
* Sad
* Angry
* Surprise
* Neutral

---

## Technologies Used

* Python
* Flask
* OpenCV
* Hugging Face Transformers
* HTML, CSS, JavaScript

---

## How It Works

1. User uploads an image or uses the webcam
2. Image or frame is sent to the Flask backend
3. The Hugging Face model processes the image
4. Emotion prediction is generated
5. Result is displayed on the dashboard

---

## API Endpoints

### Upload Image

* POST /upload
* Input: Image file
* Output: Emotion and confidence score

### Webcam Detection

* POST /webcam
* Input: Frame (image blob)
* Output: Emotion and confidence score

---

## Future Improvements

* Multi-face detection
* Faster inference using ONNX or TensorRT
* Mobile application integration
* Voice assistant integration
* IoT or robotics integration

---

## Author

Praveen Thumma

---

