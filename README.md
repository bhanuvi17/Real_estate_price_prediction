# 🏡 Real Estate Price Prediction

This is a **Real Estate Price Prediction** web application built using **Flask** and **Machine Learning**. The model predicts house prices based on user inputs such as distance to the nearest MRT station, number of convenience stores, latitude, and longitude.

---

## 📌 Features

✅ Predict house prices based on user inputs  
✅ Interactive web interface using Flask  
✅ Machine Learning model trained with `scikit-learn`  
✅ Deployed on **Render**  
✅ Fully responsive UI  

---

## 📂 Project Structure

```
real_estate_app/
│── dataset.csv                # Dataset used for training
│── real_estate_model.pkl      # Trained ML model
│── model_training.ipynb       # Jupyter Notebook for training
│── app.py                     # Flask app (main file)
│── templates/
│   ├── index.html             # Frontend UI
│── static/
│   ├── style.css              # CSS for styling
│── requirements.txt           # Dependencies
│── Procfile                   # Render deployment config
│── README.md                  # Project info
│── .gitignore                 # Ignore unnecessary files
```

---

## 🎯 Technologies Used

- **Backend:** Flask  
- **Frontend:** HTML, CSS  
- **Machine Learning:** Scikit-Learn, Pandas, NumPy  
- **Deployment:** Render  

---

## 🔧 Installation & Setup

### 🔹 Clone the Repository
```bash
git clone https://github.com/your-username/real_estate_app.git
cd real_estate_app
```

### 🔹 Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Run the Flask App
```bash
python app.py
```

🔗 Open in your browser: **http://127.0.0.1:5000/**  

---

## 🚀 Deploying on Render  

### 1️⃣ **Push Code to GitHub**  
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 2️⃣ **Deploy on Render:**  
- Go to [Render](https://render.com/)  
- Click **New Web Service**  
- Connect to your GitHub repository  
- Set **Start Command:** `gunicorn app:app`  
- Click **Deploy** 🎉  

---
🚀 Live Website  
<https://real-estate-price-prediction-ml19.onrender.com/>

## 📸 Screenshots

### 🔹 **Web Interface**
![Web App Screenshot](https://raw.githubusercontent.com/bhanuvi17/Real_estate_price_prediction/main/Screenshot%202025-02-09%20022645.png)

### 🔹 **Prediction Output**
![Prediction Output](https://raw.githubusercontent.com/bhanuvi17/Real_estate_price_prediction/main/Screenshot%202025-02-09%20022742.png)

---

## 🏆 Future Enhancements  

✅ Add more advanced ML models (e.g., Random Forest, Neural Networks)  
✅ Improve UI with interactive charts (e.g., Plotly, Dash)  
✅ Add a database to store user inputs and predictions  

---

## 📜 License  

This project is **open-source** under the [MIT License](LICENSE).  

---

### 💡 **Need Help?**  
Feel free to **open an issue** or **contribute** to improve this project! 😊  
⭐ If you like this project, give it a **star** on GitHub! ⭐  
