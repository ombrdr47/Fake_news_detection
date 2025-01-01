# 🕵️ Fake News Detector  

This project is a **Streamlit-based application** that classifies news articles as either **Fake** or **Real** using a trained **LSTM** model. The app provides an interactive and user-friendly interface for evaluating the authenticity of news content.

---

## 🚀 Features  

- **Interactive Interface:** Paste any news content and get a prediction instantly.  
- **Deep Learning Model:** Powered by an LSTM model for accurate classification.  
- **Custom Styling:** Enhanced visuals for an intuitive user experience.  
- **Real-Time Predictions:** Quickly determine if news is fake or real.  

---

## 🛠️ Setup Instructions  

Follow these steps to set up and run the application:

### 1️⃣ Clone the Repository  
Clone this repository to your local system:  

```bash  
git clone https://github.com/your-username/fake-news-detector.git  
```  

### 2️⃣ Navigate to the Project Directory  
Move into the project folder:  

```bash  
cd fake-news-detector  
```  

### 3️⃣ Install Dependencies  
Install the required Python packages using the following command:  

```bash  
pip install -r requirements.txt  
```  

### 4️⃣ Run the Application  
Launch the Streamlit app:  

```bash  
streamlit run app.py  
```  

---

## 📂 File Structure  

```
fake-news-detector/
│
├── app.py                  # Streamlit app file
├── models/
│   └── LSTM_model.keras    # Trained LSTM model
├── tokenizer.pkl           # Tokenizer used for text preprocessing
├── data/
│   ├── True.csv            # Dataset for real news
│   └── Fake.csv            # Dataset for fake news
├── requirements.txt        # List of dependencies
└── README.md               # Documentation file
```

---

## 📊 Dataset  

The app uses a labeled dataset containing two categories of news articles:  

1. **True.csv:** Real news articles.  
2. **Fake.csv:** Fake news articles.  

Each category is combined into a single dataset for model training and evaluation.  

---

## 🧪 Model Details  

- **Architecture:** LSTM-based Bidirectional RNN  
- **Embedding:** Word embeddings with a vocabulary size derived from the dataset  
- **Layers:**  
  - Embedding Layer  
  - Bidirectional LSTM  
  - Dense Layers with ReLU and Sigmoid activations  

---

## 📈 Results  

- **Accuracy:** Achieved a high test accuracy on validation data.
- **Confusion Matrix:** Provides insights into model performance on real vs. fake news classification.

---

## 🎨 Screenshots  

### Home Page  
![Home Page](https://via.placeholder.com/800x400.png?text=Screenshot+Placeholder)  

---

## ⚙️ About  

This application was developed to address the challenge of identifying fake news using natural language processing (NLP) and deep learning techniques.  

---

## 📜 License  

This project is licensed under the MIT License.  

Feel free to contribute to the project or share feedback!  

---

