from flask import Blueprint, request, jsonify
import joblib
import numpy as np
import os

predict_blueprint = Blueprint("predict", __name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), "../models/iris_model.pkl")
model = joblib.load(model_path)

@predict_blueprint.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        prediction = model.predict(np.array(data["input"]).reshape(1, -1))
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
