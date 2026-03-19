from transformers import pipeline
from PIL import Image

# Load once
classifier = pipeline(
    "image-classification",
    model="dima806/facial_emotions_image_detection"
)

def predict_emotion(image_path):
    image = Image.open(image_path)
    result = classifier(image)
    top = max(result, key=lambda x: x['score'])
    return top['label'], round(top['score'], 2)