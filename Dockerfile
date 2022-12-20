# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 8080/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .
COPY config.py .
ADD application /app/application

# Specify the command to run on container start
CMD [ "python", "./app.py" ]