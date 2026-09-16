FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container
COPY . .

# Install dependencies without caching to keep the image small
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Start the app with Gunicorn:
#   -w 4            : 4 worker processes
#   -b 0.0.0.0:7860 : bind to port 7860 on all interfaces (Hugging Face Spaces port)
#   app:learn_api   : run the Flask instance 'learn_api' defined in app.py
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:learn_api"]
