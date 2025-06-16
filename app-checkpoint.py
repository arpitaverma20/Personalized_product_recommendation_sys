from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the saved model and encoders
with open('recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

le_category = encoders['category_encoder']

# Load product data to show recommendations
product_data = pd.read_csv('product_data.csv')

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    category = request.form.get('category')
    feature1 = float(request.form.get('feature1'))
    feature2 = float(request.form.get('feature2'))

    try:
        category_encoded = le_category.transform([category])[0]
    except ValueError:
        return jsonify({'error': 'Unknown category'})

    input_features = [[category_encoded, feature1, feature2]]
    distances, indices = model.kneighbors(input_features)

    recommended_products = product_data.iloc[indices[0]].to_dict(orient='records')

    return jsonify(recommended_products)

if __name__ == '__main__':
    app.run(debug=True)
