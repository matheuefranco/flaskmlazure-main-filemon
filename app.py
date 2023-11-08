import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)
model = pickle.load(open("model.pkl", "rb"))
#names = pickle.load(open("names.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    pred = model.predict(final_features)
    #output = pred[0]
    output = ("Maligno" if pred[0] == 'M' else "Benigno")
    return render_template("index.html", prediction_text="Classificação: " + output)

@app.route("/api", methods=["POST"])
def results():
    data = request.get_json(force=True)
    pred = model.predict([np.array(list(data.values()))])
    #output = names[pred[0]]
    output = ("Maligno" if pred[0] == 'M' else "Benigno") 
    return jsonify(output)

@app.route("/apinames", methods=["GET"])
def getnames():
    nameslist = names.tolist()
    return jsonify(nameslist)
