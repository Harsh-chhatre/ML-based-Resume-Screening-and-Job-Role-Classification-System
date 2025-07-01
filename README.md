Resume Screening and Job Role Classification System

A machine learning-powered web application that classifies resume text into job categories such as Data Science, HR, Web Development, etc., using Natural Language Processing (NLP) and a Naive Bayes classifier.

📌 Project Overview

This project automates resume screening by analyzing the textual content and predicting the most relevant job role. It uses NLP for text cleaning and feature extraction, and a trained machine learning model to classify resumes. The web interface is built using Flask, allowing users to paste resume content and instantly get category predictions.

🚀 Features

- ✅ Resume text preprocessing with NLP (tokenization, stopword removal, stemming)
- ✅ TF-IDF vectorization for feature extraction
- ✅ Classification using Multinomial Naive Bayes
- ✅ Clean and colorful web interface with Flask
- ✅ Real-time predictions on the browser

🛠️ Tech Stack

- Frontend: HTML5, CSS3 (inline styling)
- Backend: Python, Flask
- Machine Learning: Scikit-learn, NLTK, Pandas
- Deployment: Localhost (Flask dev server)

📂 Project Structure

resume-screening-app/
├── app2.py                 # Flask application
├── resume_model.pkl        # Trained Naive Bayes model
├── tfidf_vectorizer.pkl    # Saved TF-IDF vectorizer
├── templates/
    └── index.html          # Frontend UI (form and results)

🧪 How to Run Locally

1. Clone the Repository
   git clone https://github.com/your-username/Resume Screening and Job Role Classification System.git
   cd resume-screening-app

2. Install Requirements
   pip install -r requirements.txt

3. Run the Flask App
   python app.py

4. Open in Browser
   Visit http://127.0.0.1:5000/ and try it out!

📝 Sample Input (Resume Text)

Experienced Python developer with knowledge of machine learning, data analysis, and pandas...

🎯 Output
Predicted Category: Data Science

✨ Author

- Harsh Chhatre
