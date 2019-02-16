FROM python:3.6-alpine
MAINTAINER Carl Njoku "flavoursoft@yahoo.com"
COPY . /app
WORKDIR /app
RUN apk update 
RUN apk update install -y software-properties-common vim
RUN apk-add-repository ppa:jonathonf/python-3.6
RUN apk update

RUN apk update install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apk update install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["image_upload.py"]


