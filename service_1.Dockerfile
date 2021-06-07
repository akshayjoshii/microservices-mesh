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
COPY enter_password_service.py /app/enter_password_service.py

ADD  static /app/static
ADD templates /app/templates

RUN pip install -r requirements.txt --src /usr/local/src

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["/app/enter_password_service.py"]