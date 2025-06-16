# Personalized_product_recommendation_sys

This project is a machine learning-based chatbot system that recommends personalized products (like skincare and haircare items) based on user input. It uses a CSV dataset for training and Flask for the backend web interface.

---

## 💡 Features

- Chat-based product recommendation system
- Trained ML model using product features from CSV
- Flask backend serving HTML-based chat interface
- Encoders for feature and label processing
- Modular code for easy updates and scalability

---

## 🛠️ Tech Stack

- **Python**
- **Flask** (Web framework)
- **Pandas**, **NumPy** (Data manipulation)
- **Scikit-learn** (Model training and encoding)
- **CSV** file (`product_data.csv`) as the dataset
- **HTML/CSS** for frontend chat interface

---

## 📁 Project Structure
├── templates/
│ ├── chat.html
│ └── index.html
├── app1.py # Main Flask application
├── product_data.csv # Product dataset (CSV format)
├── product_model.pkl # Trained ML model
├── feature_encoders.pkl # Encoded input features
├── product_label_encoder.pkl # Encoded product labels
├── encoders.pkl # Combined encoders (if used)
├── recommendation_model.pkl # (Optional) another saved model
├── Untitled.ipynb # Jupyter Notebook (for experiments)
├── requirements.txt # Python dependencies (create it)
└── README.md

