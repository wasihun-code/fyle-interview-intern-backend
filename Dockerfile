# Use a base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose the port your Flask app listens on
EXPOSE 5000

# Run your Flask application
CMD ["bash", "run.sh"]