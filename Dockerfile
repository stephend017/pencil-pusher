# OLD STUFF

# FROM python:3-slim AS builder
# ADD . /container/app
# WORKDIR /container/app

# # Example dependency install
# RUN pip install --target=/container/app -r requirements.txt

# # A distroless container image with Python and some basics like SSL certificates
# # https://github.com/GoogleContainerTools/distroless
# FROM gcr.io/distroless/python3-debian10
# COPY --from=builder /container/app /container/app
# WORKDIR /container/app
# ENV PYTHONPATH /container/app
# CMD ["/container/app/ghapd/__main__.py"]


# NEW SHIT
FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN apt update -y && \
    apt install git -y

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD ["ghapd/__main__.py"]
