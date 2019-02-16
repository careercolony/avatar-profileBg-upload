FROM python:3.6-alpine
MAINTAINER Carl Njoku "flavoursoft@yahoo.com"
COPY . /app
WORKDIR /app
RUN python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["image_upload.py"]


