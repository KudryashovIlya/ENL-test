FROM selenium/standalone-chrome-debug:latest
RUN apt-get install python3
RUN pip3 install selenium

RUN apt-get install wget
RUN wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip -P /tmp
RUN unzip /tmp/chromedriver_linux64.zip -d /tmp/

