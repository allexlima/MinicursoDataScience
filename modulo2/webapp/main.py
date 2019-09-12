from flask import Flask, render_template, request
from ai_ml import predictor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/api", methods=['POST'])
def api():
    payload = request.form.to_dict()
    return predictor(payload)

if __name__ == "__main__":
    app.run(port=5000, debug=True)