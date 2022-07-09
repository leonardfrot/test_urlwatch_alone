FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3.9
RUN apt install -y python3-pip

# for pdftotext
RUN apt-get update
RUN yes | apt-get install build-essential libpoppler-cpp-dev pkg-config python-dev


COPY / /urlwatch
WORKDIR /urlwatch

RUN pip install -r urlwatch/requirements.txt

RUN playwright install --with-deps chromium

CMD urlwatch/start.sh