from flask import Flask, request, jsonify
from flask_cors import CORS 
from model.detector import load_model, detect_text

# Initialize Flask app
app = Flask(__name__)
# Enable CORS for all routes, all origins
CORS(app)  

# Load the model when server starts
model = load_model()

# Root endpoint
@app.route('/', methods=['GET'])
def read_root():
    return jsonify({"message": "AI Text Detector is running"})

# Detection endpoint
@app.route('/detect', methods=['POST'])
def detect():
    # Get JSON data from request
    data = request.get_json()
    if not data or 'text' not in data or not data['text'].strip():
        return jsonify({"error": "Text cannot be empty"}), 400
    
    try:
        # Predict with model
        result = detect_text(model, data['text'])
        # Format response for frontend
        label = "Human" if result["label"] == 0 else "AI"
        return jsonify({
            "result": label,
            "confidence": float(result["confidence"])
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)