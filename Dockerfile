FROM ubuntu:16.10
MAINTAINER Carl Njoku "flavoursoft@yahoo.com"
RUN apt-get update -y
RUN apt-get install -y python-pip3 python3.6 build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["image_upload.py"]


