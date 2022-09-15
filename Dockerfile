# dockerdile, Image, Container
FROM --platform=linux/amd64 python:3.9

WORKDIR /code

EXPOSE 80

ADD app.py .

COPY . /code

RUN pip install --upgrade pip \
    && pip install numpy \
    && pip install pandas \
    && pip install flask \
    && pip install sklearn

ENTRYPOINT ["python"]
CMD ["app.py"]

