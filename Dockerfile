FROM python:3.6.6-alpine
MAINTAINER Carl Njoku "flavoursoft@yahoo.com"
COPY . /app
WORKDIR /app

# update pip
RUN python3.6.6 -m pip install pip --upgrade
RUN python3.6.6 -m pip install wheel
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["image_upload.py"]


