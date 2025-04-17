Simple Time Service – Setup Guide
This guide walks you through building and deploying a simple Python-based microservice that returns a timestamp and the visitor's IP address. The app is containerized using Docker and hosted on DockerHub and GitHub.

✅ Prerequisites
Install the following tools:

Git

Docker Desktop

Visual Studio Code

In VS Code, install the following extensions:

Docker

Python

Git

📁 Project Setup
Create a folder
In VS Code:
File → New Folder → Name it simple-time-service

Add Python script
Inside the folder, create a new file app.py and write your application code.

Create requirements file
Add a file named requirements.txt and list all required Python packages.

Install dependencies (optional check)
Open the terminal in VS Code and run:

pip install -r requirements.txt
python app.py
Your app should now be accessible at:
http://<your-local-ip>:5000

🐳 Dockerize the Application
Create a Dockerfile
In the same directory, add a file named Dockerfile and add the relevant image build instructions (see repo for example).

Build the Docker image

docker build -t simpletimeservice .
Run the Docker container

docker run -p 5000:5000 simpletimeservice
Test your app
Visit http://localhost:5000 in your browser and verify that the output includes the IP and timestamp.

📤 Push Docker Image to DockerHub
Login to DockerHub

docker login
Tag the image

docker tag simpletimeservice your-dockerhub-username/simpletimeservice
Push the image

docker push your-dockerhub-username/simpletimeservice
🚀 Push Code to GitHub
Initialize Git and push to GitHub

git init
git add .
git remote add origin https://github.com/saisivapriya695/simpletimeapp.git
git branch -M main
git push -u origin main
Your code will now be available at: GitHub Repository

