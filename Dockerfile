# Use a lightweight Python image
FROM python:3.9-slim

WORKDIR /app

# Copy the required files
COPY requirements.txt .
COPY app.py .

RUN echo ${PWD} && ls -lR

COPY model /model  # Assuming the model is stored in the "model" folder

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
