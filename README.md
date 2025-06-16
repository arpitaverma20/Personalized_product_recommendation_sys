# Personalized_product_recommendation_sys

# 🧠 Personalized Product Recommendation System

This project is a machine learning-powered **chatbot** that recommends personalized skincare and haircare products based on user preferences. It leverages a **CSV dataset** for training, a **Random Forest model** for predictions, and a **Flask web app** to interact with users through a simple chat interface.

---

## 💡 Features

- 🗨️ Chat-based recommendation interface  
- 🧠 Random Forest ML model trained on product features  
- 🔄 Encoders for feature and label transformation  
- 💾 Model and data stored in `.pkl` and `.csv` formats  
- 🌐 Flask backend with interactive HTML templates  
- 🔧 Modular code for easy scalability and customization  

---

## 🛠️ Tech Stack

| Technology         | Role/Usage                                  |
|--------------------|----------------------------------------------|
| **Python**         | Core programming language                    |
| **Flask**          | Backend web framework (`app1.py`)            |
| **Pandas**, **NumPy** | Data preprocessing and manipulation     |
| **Scikit-learn**   | Model training (Random Forest), encoders     |
| **CSV**            | Dataset file (`product_data.csv`)            |
| **Pickle (.pkl)**  | Model and encoder storage                    |
| `product_model.pkl`| Trained Random Forest model                  |
| `feature_encoders.pkl`, `encoders.pkl` | Feature encoders         |
| `product_label_encoder.pkl` | Label encoder                       |
| **HTML (Jinja)**   | Frontend UI (`chat.html`, `index.html`)      |
| **Jupyter Notebook** | Model development (`Untitled.ipynb`)       |

---

## 📁 Project Structure 
├── templates/
│ ├── chat.html # Chat UI
│ └── index.html # (Optional) landing page
├── app1.py # Main Flask backend app
├── product_data.csv # Dataset for recommendations
├── product_model.pkl # Trained Random Forest model
├── feature_encoders.pkl # Encoded input features
├── product_label_encoder.pkl # Encoded product labels
├── encoders.pkl # Combined encoders (optional)
├── recommendation_model.pkl # (Optional) alternate model
├── Untitled.ipynb # Model training notebook
├── requirements.txt # Python dependencies
└── README.md # Project description

