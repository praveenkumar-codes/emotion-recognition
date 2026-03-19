from flask import Flask, render_template, request, jsonify
import os
import cv2
from model import predict_emotion

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Image Upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    emotion, score = predict_emotion(filepath)

    return jsonify({
        'emotion': emotion,
        'score': score,
        'image': filepath
    })

# Webcam Frame API
@app.route('/webcam', methods=['POST'])
def webcam():
    file = request.files['frame']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], "frame.jpg")
    file.save(filepath)

    emotion, score = predict_emotion(filepath)

    return jsonify({
        'emotion': emotion,
        'score': score
    })

if __name__ == '__main__':
    app.run(debug=True)