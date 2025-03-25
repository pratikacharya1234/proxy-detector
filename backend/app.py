from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample function to detect keywords in text
def detect_keywords(text):
    keywords = ['human', 'AI', 'sample', 'text', 'detection']
    results = {keyword: keyword in text for keyword in keywords}
    return results

@app.route('/api/detect_text', methods=["POST"])
def detect_text():
    response = request.get_json()
    text = response.get('text', '')
    
    # Perform text detection
    results = detect_keywords(text)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)