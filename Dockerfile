# Use a minimal Python image
FROM python:3.11-slim

# Create a non-root user
RUN useradd -m appuser

# Set working directory
WORKDIR /home/appuser/app

# Copy your app files
COPY --chown=appuser:appuser . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER appuser

# Expose the port (you can change this if your app runs on a different one)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
