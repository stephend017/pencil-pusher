FROM python:3-slim AS builder
ADD . /container/app
WORKDIR /container/app

# Example dependency install
RUN pip install --target=/container/app -r requirements.txt

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=builder /container/app /container/app
WORKDIR /container/app
ENV PYTHONPATH /container/app
CMD ["/container/app/ghapd/__main__.py"]
