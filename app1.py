from flask import Flask, request, jsonify, send_from_directory,render_template
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model and encoders
model = joblib.load("product_model.pkl")
le_product = joblib.load("product_label_encoder.pkl")
encoders = joblib.load("feature_encoders.pkl")

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.json

        required = ["skin_type", "hair_concerns", "allergies", "price_range"]
        if not all(field in input_data for field in required):
            return jsonify({"error": "Missing input fields"}), 400

        encoded_input = [
            encoders["skin_type"].transform([input_data["skin_type"]])[0],
            encoders["hair_concerns"].transform([input_data["hair_concerns"]])[0],
            encoders["allergies"].transform([input_data["allergies"]])[0],
            encoders["price_range"].transform([input_data["price_range"]])[0]
        ]

        pred_encoded = model.predict([encoded_input])[0]
        predicted_product = le_product.inverse_transform([pred_encoded])[0]

        return jsonify({"recommended_product": predicted_product})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
