# Minimal Dockerfile for Python app deployment
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (if using Flask, default is 5000)
EXPOSE 5000

# Start the app (update if using a different entrypoint)
CMD ["python", "app.py"]
