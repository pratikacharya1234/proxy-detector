# Import Flask and required modules
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define the detection route
@app.route('/detect', methods=['POST'])
def detect_text():
    # Get the text from the frontend request
    data = request.get_json()
    text = data.get('text', '')

    # Placeholder for your AI detection logic
    # Replace this with your actual model prediction
    if text:
        # Example: Simple dummy logic (replace with your model)
        result = "Human-written" if len(text.split()) > 10 else "AI-generated"
        confidence = 0.75  # Dummy confidence score
    else:
        return jsonify({'error': 'No text provided'}), 400

    # Return the result as JSON
    return jsonify({
        'result': result,
        'confidence': confidence
    })

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)