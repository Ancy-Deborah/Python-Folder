from flask import Flask, jsonify, request
from proC125 import  get_prediction

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Welcome"

@app.route("/predict-alphabet", methods=["POST"])
def predict_data():
 image = request.files.get("alphabet")
 prediction = get_prediction(image)
 return jsonify({"prediction": prediction}), 200
