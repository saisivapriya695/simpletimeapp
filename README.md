# simpletimeapp
this app will give you current time and date along with timestamp using python
first to complete the task we will look after the pre-requisite needed:
--------------------------------------------------------------

1.install git,docker desktop,vscode or 
2.just install vs code and in the left side you can see different icons .in that select etensions and search and install docker,python(since i prefer using python for simple time app development),git
3.your now ready to work on it.
4.now create a new folder from 
vscode------->files------------>create folder[i named it simple-time-service]------->new file 
5.inside this folder name the new file as app.py(or any as you wish to name the python script)
6.write the code needed
7.now create another file with requirements.txt name to store what are the packages that are needed to install inorder to run the app.py
[before running the commands just make sure your in the same directory in which your app.py,requirements.tt files are there]
8.just to check if app is running fine(optional): 
		1.go to the terminal in vs code and give the command   		pip install -r requirements.txt 
		2.now run the command   python app.py
9.now u should see a url with hostname you gave in the code appearing as output here in my case it is http://192.168.216.49:5000
once browsed you should see the epected output and now it means your app is successfully running on the port specified.

next step is to containerize the application using docker:
--------------------------------------------------------------

now that we have the application running let us containarze it as per constraints given.

1.as a first step create a file named docker file in simple-time-service directory
2.write code to generate image[code is in the repo i shared]
3. save it in vs code
4.make sure your docker is up and running and then run the following command to build the image
docker build -t simpletimeservice .  [dont forget the . at the end]
5.now run the image using 
docker run -p 5000:5000 simpletimeservice
6.to check if everything is running well just go to the url and check to see if ip address and timestamp are coming up
url- http://localhost:5000

now Push Image to DockerHub
---------------------------------
1. Log in to DockerHub using the command
docker login
It’ll ask for your username and password (or personal access token if you have 2FA).
2.then give a tag for your image using:
docker tag simpletimeservice your-dockerhub-username/simpletimeservice
3. Push the image using:
docker push your-dockerhub-username/simpletimeservice

clone code to git
-----------------------------------
1.make sure u have a git account and new repository created already.here i created a repo called simpletimeapp
2.now initialize a local repository by going to same directory where the code related files reside in and run the following commands in powershell
A. git init
B. git add .
c. git remote add origin https://github.com/saisivapriya695/simpletimeapp.git
d. git branch -M main
e. git push -u origin main
now u should see that all the files are already being cloned to git repo if checked url.
my repo url for all the codes:
--------------------------------
URL:  https://github.com/saisivapriya695/simpletimeapp.git




