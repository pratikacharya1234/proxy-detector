import pickle
import os
from sklearn.linear_model import LogisticRegression
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download NLTK data (run once)
nltk.download('punkt_tab', quiet=True)  

# Feature extraction function
def extract_features(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    return [
        len(words),              # Word count
        len(sentences),          # Sentence count
        len(words) / max(len(sentences), 1)  # Avg sentence length
    ]

# Load text from file or use default
def load_sample(file_path, default_text):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return default_text

# Training data (load from files or use defaults)
def get_training_data():
    human_file = 'backend/data/Human_written.txt'
    ai_file = 'backend/data/Ai_written.txt'
    

    human_sample = load_sample(human_file)
    ai_sample = load_sample(ai_file)
    
    X = [
        extract_features(human_sample),  # Human features
        extract_features(ai_sample)      # AI features
    ]
    y = [0, 1]  # 0 = human, 1 = AI
    return X, y

# Train and save model
def train_model():
    X, y = get_training_data()
    model = LogisticRegression()
    model.fit(X, y)
    
    # Ensure directory exists and save model
    os.makedirs("backend/model", exist_ok=True)
    model_path = "backend/model/trained_model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    return model

# Load model (train if not exists or invalid)
def load_model():
    model_path = "backend/model/trained_model.pkl"
    if not os.path.exists(model_path) or os.path.getsize(model_path) == 0:
        return train_model()
    try:
        with open(model_path, "rb") as f:
            return pickle.load(f)
    except (EOFError, pickle.UnpicklingError):
        # If loading fails (e.g., corrupted file), retrain
        return train_model()

# Detect text (predict with model)
def detect_text(model, text):
    features = extract_features(text)
    label = model.predict([features])[0]
    confidence = model.predict_proba([features])[0][label]
    return {"label": label, "confidence": confidence}