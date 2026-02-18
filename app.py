from flask import Flask, request, jsonify
from src.predict import predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def prediction():
    data = request.json
    result = predict(data["text"])
    return jsonify({"sentiment": result})

if __name__ == "__main__":
    app.run(debug=True)
