# Use the official FastAPI image (which includes uvicorn and ASGI)
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the local requirements.txt file to the container
COPY ./app/requirements.txt /app/requirements.txt

COPY .env /app/.env

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY ./app /app

COPY .env /app/.env

# Expose the port that your FastAPI app will run on (change if needed)
EXPOSE 8000

# Command to start the FastAPI server
CMD ["uvicorn", "kendra_api:app", "--host", "0.0.0.0", "--port", "8000"]
