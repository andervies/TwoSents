# TwoSents
## **Sentiment Analysis API**  
🚀 A FastAPI-based sentiment analysis API using DistilBERT. This project loads a fine-tuned TensorFlow model and classifies text as **Positive** or **Negative**.

### **Features**  
- FastAPI backend for quick inference  
- TensorFlow/Keras-based DistilBERT model  
- Tokenization using Hugging Face  
- JSON API response with sentiment and confidence score  
- **Dockerized for easy deployment**  

### **Dataset**  
This model was fine-tuned using an **Amazon product review dataset**.  

### **Installation**  
#### **Run Locally**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/andervies/sentiment-analysis-api.git
   cd sentiment-analysis-api
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API:  
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

#### **Run with Docker**  
1. **Build the Docker image**:  
   ```bash
   docker build -t sentiment-analysis-api .
   ```
2. **Run the container**:  
   ```bash
   docker run -p 8000:8000 sentiment-analysis-api
   ```

### **Usage**  
Send a POST request with text input:  
```bash
curl -X 'POST' 'http://localhost:8000/predict' \
     -H 'Content-Type: application/json' \
     -d '{"text": "This product is amazing!"}'
```

Expected response:  
```json
{
  "text": "This product is amazing!",
  "sentiment": "Positive",
  "confidence": 0.98
}
```

### **License**  
MIT License
