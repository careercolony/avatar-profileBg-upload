FROM python:3.6-alpine
MAINTAINER Carl Njoku "flavoursoft@yahoo.com"
RUN python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["image_upload.py"]


