from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("real_estate_model.pkl")
scaler = joblib.load("scaler.pkl")

app = Flask(__name__)

# Route for Home Page
@app.route("/")
def home():
    return render_template("index.html")

# API Endpoint for Prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data from request
        data = request.json
        values = [float(data["house_age"]), float(data["distance_to_mrt"]), float(data["num_convenience_stores"]), float(data["latitude"]), float(data["longitude"])]
        
        # Scale input
        scaled_values = scaler.transform([values])
        
        # Make prediction
        prediction = model.predict(scaled_values)[0]
        
        # Ensure non-negative output
        prediction = max(0, prediction)

        return jsonify({"predicted_price": round(prediction, 2)})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
