import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load the model and tokenizer
model = load_model('models/LSTM_model.keras')
with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

# Page configuration
st.set_page_config(page_title="Fake News Detector", page_icon="🕵️", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
        color: #333333;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stTextInput, .stTextArea {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
    }
    .result {
        font-weight: bold;
        font-size: 20px;
        color: #007BFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main title
st.title("🕵️ Fake News Detector")
st.markdown("""_Enter the content of the news article below and click 'Predict' to determine if it's fake or real._""")

# Input box for news content
news = st.text_area("Paste the news article here:", placeholder="Type or paste the content of the news article...")

# Prediction button
if st.button("Predict"):
    if not news.strip():
        st.error("Please enter the news content before predicting.")
    else:
        with st.spinner("Analyzing the content..."):
            sequence = tokenizer.texts_to_sequences([news])
            padded_sequence = pad_sequences(sequence, maxlen=40, padding='post', truncating='post')
            prediction = model.predict(padded_sequence)
            result = "Real" if prediction > 0.5 else "Fake"
        
        # Display the result
        st.markdown(f"<p class='result'>The news is: <strong>{result}</strong></p>", unsafe_allow_html=True)

# Footer
st.markdown("""---
### 🔧 About
This tool uses an LSTM model to analyze and classify news content as either **fake** or **real**. The underlying model is trained on a labeled dataset of news articles.
""")
