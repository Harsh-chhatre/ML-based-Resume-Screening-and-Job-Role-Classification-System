# 🧠 Resume Screening and Job Role Classification System

A machine learning-powered web application that classifies resume text into job categories such as **Data Science**, **HR**, **Web Development**, etc., using Natural Language Processing (NLP) and a Naive Bayes classifier.

---

## 📌 Project Overview

This project automates resume screening by analyzing textual content and predicting the most relevant job role. It uses NLP for text cleaning and feature extraction, and a trained machine learning model to classify resumes. The web interface is built using **Flask**, allowing users to paste resume content and get instant predictions.

---

## 🚀 Features

- 🧹 Resume text preprocessing (tokenization, stopword removal, stemming)
- 📈 TF-IDF vectorization for feature extraction
- 📊 Classification using Multinomial Naive Bayes
- 🌐 Flask-powered web application
- 🎨 Colorful and responsive UI

---

## 🛠️ Tech Stack

| Layer       | Technology             |
|-------------|------------------------|
| Frontend    | HTML5, CSS3 (inline)   |
| Backend     | Python, Flask          |
| ML/NLP      | Scikit-learn, NLTK, Pandas |
| Deployment  | Flask Dev Server (localhost) |

---

## 📂 Folder Structure
```
resume-screening-app/
│
├── app.py               # Flask web application
├── resume_model.pkl     # Trained ML model
├── tfidf_vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates folder
  └── index.html         # Web UI for resume input/output
```
---

## 🧪 How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Resume Screening and Job Role Classification System.git
   cd resume-screening-app

---

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt

---

3. **Run the Flask App**
   ```bash
   python app.py

---

## 📝 Sample Input (Resume Text)
```
Experienced Python developer with knowledge of machine
learning, data analysis, and pandas...
```
---

## 🎯 Output
Predicted Category: Data Science

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## ✨ Author

- Harsh Chhatre

