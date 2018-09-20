import os

from flask import (
    Flask,
    jsonify,
    request,
)
from werkzeug.utils import secure_filename
from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

from .constants import UPLOAD_FOLDER
from .model import load_model

app = Flask(__name__)
model = None


@app.route('/predict', methods=['POST'])
def predict():
    # Getting the image
    if not request.files['image']:
        return None

    filename = secure_filename(request.files['image'].filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    request.files['image'].save(path)

    # Apply predictions
    global model
    if model is None:
        model = load_model()

    image = Image.open(path)
    image = image.resize((224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    predictions = model.predict(image)
    results = imagenet_utils.decode_predictions(predictions)

    predictions = [
        {
            "label": label,
            "probability": float(probability)
        } for (_, label, probability) in results[0]
    ]

    return jsonify(predictions)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
