FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04
MAINTAINER Carl Njoku "flavoursoft@yahoo.com"
RUN apt-get update -y
# pip has to be installed before setuptools, setuptools has to be installed before tensorflow
RUN python3.6 -m pip install --no-cache-dir -U pip
RUN python3.6 -m pip install --no-cache-dir -U setuptools
# also useful
RUN python3.6 -m pip install --no-cache-dir ipython requests numpy pandas quandl
RUN python3.6 -m pip install --no-cache-dir tensorflow-gpu==1.3.0rc0
RUN ln -s /usr/bin/python3.6 /usr/bin/python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["image_upload.py"]


