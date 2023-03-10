# Use an official Python runtime as the base image
FROM python:3.7-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip3 install streamlit
RUN pip3 install watchdog
RUN pip3 install pymongo
RUN pip3 install requests


# Set environment variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Run the Streamlit app
CMD streamlit run app.py