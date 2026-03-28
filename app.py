from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("models/model.pkl","rb"))

@app.route("/")
def home():
    return "Energy Prediction API Running"

@app.route("/predict", methods=["POST"])

def predict():

    data = request.json

    temp = data["temperature"]
    humidity = data["humidity"]
    wind = data["wind_speed"]

    prediction = model.predict([[temp, humidity, wind]])

    return jsonify({"prediction": float(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)