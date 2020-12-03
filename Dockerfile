FROM python:3.8

RUN pip3 install selenium

RUN apt-get install wget
RUN wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip -P /tmp
RUN unzip /tmp/chromedriver/chromedriver_linux64.zip

