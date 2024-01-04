FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

COPY main.py .
# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY ./app ./app

# Command to run on container start
CMD ["python3", "main.py"]
