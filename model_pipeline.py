import tensorflow as tf
from transformers import TFBertForSequenceClassification, BertTokenizer, TFDistilBertForSequenceClassification
import numpy as np


class SentimentAnalyzer:
    def __init__(self, model_path, tokenizer_name='bert-base-uncased'):
        self.model = TFDistilBertForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = BertTokenizer.from_pretrained(tokenizer_name)
        self.labels = ['Negative', 'Positive']

    def predict(self, texts, batch_size=32):
        # Tokenize inputs
        tokenized_inputs = self.tokenizer(
            texts,
            truncation=True,
            padding=True,
            return_tensors="tf",
            max_length=128
        )

        # Get predictions
        outputs = self.model.predict(tokenized_inputs["input_ids"], batch_size=batch_size)
        predictions = tf.nn.softmax(outputs[0], axis=1)
        predicted_labels = [self.labels[pred] for pred in tf.argmax(predictions, axis=1)]

        return predicted_labels