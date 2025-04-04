from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from model_pipeline import SentimentAnalyzer

app = FastAPI()
model_path = "/app/model/"
analyzer = SentimentAnalyzer(model_path)


class TextRequest(BaseModel):
    text: Union[str, list[str]]



@app.post("/predict")
async def predict_sentiment(request: TextRequest):
    if isinstance(request.text, str):
        texts = [request.text]
    else:
        texts = request.text

    predictions = analyzer.predict(texts)

    if isinstance(request.text, str):
        return {"sentiment": predictions[0]}
    else:
        return {"sentiments": predictions}