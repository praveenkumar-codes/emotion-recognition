# Emotion Recognition System

A real-time Image-Based Emotion Recognition System built using Deep Learning and Hugging Face pre-trained models.
This application detects human emotions from uploaded images and live webcam input through a web interface.

---

## Features

* Real-time Webcam Emotion Detection
* Image Upload and Emotion Prediction
* Pre-trained Deep Learning Model (Hugging Face)
* Web-based Dashboard using Flask
* Fast and Accurate Predictions

---

## Project Structure

```
emotion-recognition/
│
├── static/              # CSS, JS, uploaded images
├── templates/           # HTML files (UI)
│
├── app.py               # Flask backend
├── model.py             # Emotion prediction logic
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/emotion-recognition.git
cd emotion-recognition
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

dima806/facial_emotions_image_detection

The model is already trained and ready for inference.

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
2. Image/frame is sent to the Flask backend
3. The model processes the input
4. Emotion is predicted
5. Result is displayed on the web page

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


## Author

Praveen Thumma

---

