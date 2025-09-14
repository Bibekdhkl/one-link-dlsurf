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
EXPOSE 2000

# Start the app on port 2000
CMD ["python", "app.py"]
