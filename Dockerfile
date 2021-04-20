FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN apt update -y && \
    apt install git -y

WORKDIR /

# no version is set here, only set version on releases
RUN pip3 install pencil-pusher==1.5.2

CMD ["python3", "-m", "pencil_pusher"]
