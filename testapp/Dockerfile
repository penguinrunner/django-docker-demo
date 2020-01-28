FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

#copies current directory code into working directory
COPY . /app/

RUN pip install -r requirements.txt

# this is an automated script added for running commands when the container is built
# MAKE SURE YOU CHANGE LINE ENDINGS IN Notepad++ to "LF" instead of "CR LF"
RUN chmod +x entrypoint.sh

