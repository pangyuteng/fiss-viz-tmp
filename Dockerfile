FROM tensorflow/tensorflow:2.4.1-gpu-jupyter

WORKDIR /opt
RUN /usr/bin/python3 -m pip install --upgrade pip
COPY requirements.txt /opt
RUN pip install -r requirements.txt --use-feature=2020-resolver
RUN pip install git+https://www.github.com/keras-team/keras-contrib.git