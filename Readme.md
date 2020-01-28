## Steps for Configuring a Django project in Docker and creating a Dockerhub image for Continuous Deployment
#### I would not clone this whole repo, but you can. You will understand it much better if you create the files yourself.
This is mostly for my own sanity and reference later, but if you find it helpful then thats good too :) 
##### - Local Setup 
- Create a Docker Project Folder Ex: docker_my_app
- Create a `docker-compose.yml` file in project folder
- Create folder for nginx
- Create config file `nginx.conf` in the nginx folder
- Create the `Dockerfile` for nginx in the nginx folder (will reference config file)
    - This file will also need created in production (Unless you build your own nginx image as well)
- Copy your Django application into project folder (Ex: testapp)
- Add Gunicorn to `requirements.txt` if not already there
- copy `.gitignore` to `.dockerignore` in the application folder to exclude stuff in docker image
    - This is your `.gitignore` from your application, not mine
- Create `entrypoint.sh` in application folder for running commands once the container is up (ex `manage.py migrate` or management commands)
    - If you are on windows make sure you change your line endings for this file to LF 
    instead of CRLF or it will fail. Just click on the bottom of Notepad++ or whatever your using.
- Create a Dockerfile in application folder for python image
    - This file will become bundled in our custom python image with our app
    - This file will not be created manually in production
- Create django.env file in Docker Project folder (Not in the application folder)
    - This stores super secret logins for your django app to use, like the database credentials
    - This assumes in your Django settings your using `os.getenv('DB_NAME')`, `os.getenv('DB_USER')`, ect...
    - This file will need to manually created in production
- The compose file has 4 services
    - The app (Django)
    - Nginx (acting as a reverse proxy / web server for static files)
    - The database using postgres
    - Watchtower (Optional) to automatically pull new images down and replace
     containers (Continuous Deployment) from DockerHub
- Run "docker-compose up -d --build"
- If you used my compose file then your app should be running on port 9000
    
##### - Creating Repository
- Your Django application should now be ready to put into a repo on docker
- I used the github account linking with automatic build turned on
- You can also use the docker cli to push it to docker but... come on.
- Make sure you only push your application folder and not the whole docker project folder.
    
    
##### - Production / Staging server 
- Create Docker Project Folder Ex: docker_my_app
- Create `docker-compose.yml` file in project folder
    - This is the production version.
    - Removed the "Build" Settings and replaced with Image (Your repo) for your application.
    - I commented the parts in both versions of the compose file so you can see the difference. 
- Create folder for nginx
- Create the `Dockerfile` for nginx in the nginx folder (will reference config file)
- Create django.env file in Docker Project folder 
- Run "docker-compose up -d --build"


##### Notes
There is also a `docker-compose-simple.yml` if you just want to run the Django development 
server in a container for the sake of playing with docker

I know I could create my own nginx image and only have literally two files
on my production server, but you only get one free private repo on Dockerhub. So I didnt.



