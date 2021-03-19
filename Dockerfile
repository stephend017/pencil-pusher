FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN apt update -y && \
    apt install git -y

WORKDIR /

RUN pip3 install pencil-pusher

CMD ["python3", "-m", "pencil_pusher"]
