FROM python:3.8-slim

LABEL maintainer = "poojitha.vijayanarasimha@sap.com"

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-dev \
    build-essential

WORKDIR /app

ENV FLASK_ENV=development

COPY requirements.txt /app/requirements.txt
COPY definition.py /app/definition.py
COPY check_password_repeated_service.py /app/check_password_repeated_service.py

RUN pip install -r requirements.txt --src /usr/local/src

ADD  static /app/static

EXPOSE 5002
ENTRYPOINT ["python"]
CMD ["/app/check_password_repeated_service.py"]