import pickle
import os
from sklearn.linear_model import LogisticRegression
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download NLTK data (run once)
nltk.download('punkt', quiet=True)

# Feature extraction function
def extract_features(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    return [
        len(words),              
        len(sentences),          
        len(words) / max(len(sentences), 1) 
    ]

# Training data (two samples)
def get_training_data():
    # Read file contents
    with open('data/Human_written.txt', 'r', encoding='utf-8') as file:
        human_sample = file.read()
    with open('data/Ai_written.txt', 'r', encoding='utf-8') as file:
        ai_sample = file.read()
    
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
    
    # Save model to file
    with open("backend/model/trained_model.pkl", "wb") as f:
        pickle.dump(model, f)
    return model

# Load model (train if not exists)
def load_model():
    model_path = "backend/model/trained_model.pkl"
    if not os.path.exists(model_path):
        return train_model()
    with open(model_path, "rb") as f:
        return pickle.load(f)

# Detect text (predict with model)
def detect_text(model, text):
    features = extract_features(text)
    label = model.predict([features])[0]
    confidence = model.predict_proba([features])[0][label]
    return {"label": label, "confidence": confidence}