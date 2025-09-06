import cv2
import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("waste_model.h5")

CATEGORIES = ["Plastic", "Paper", "Metal", "Organic", "Glass"]

def prepare_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    return np.expand_dims(img, axis=0)

def classify(image_path):
    image = prepare_image(image_path)
    prediction = model.predict(image)
    class_idx = np.argmax(prediction)
    print(f"Predicted: {CATEGORIES[class_idx]}")

if __name__ == "__main__":
    classify("data/sample_images/test1.jpg")
