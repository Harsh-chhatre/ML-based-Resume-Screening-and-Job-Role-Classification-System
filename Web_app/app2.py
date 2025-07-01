from flask import Flask, render_template, request
import joblib

# Load model and vectorizer
model = joblib.load("resume_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        resume_text = request.form["resume"]

        # Clean the resume using same steps as before (optional)
        # Here we assume model already trained on raw text (TF-IDF)
        transformed = vectorizer.transform([resume_text])
        prediction = model.predict(transformed)[0]

        return render_template("index.html", result=prediction)

if __name__ == '__main__':
    app.run(debug=True)
