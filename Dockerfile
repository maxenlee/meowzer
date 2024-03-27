FROM python:3-alpine3.15
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
# EXPOSE 3000
COPY . /app
CMD python ./index.py
COPY Dockerfile /

# docker build -t maxenlee/hey-python-flask:x.x.x.RELEASE .
# docker container run -d -p 3000:3000 -v $PWD:/app --name flask --rm  maxenlee/hey-python-flask:0.0.6.RELEASE
# github URL
# Dockerhub URL
