# Use an official Python runtime as base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy only necessary files (improves Docker caching)
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python", "main.py"]
