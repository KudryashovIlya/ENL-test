FROM selenium/standalone-chrome-debug:latest
RUN sudo apt-get update

RUN sudo apt-get install -y python3 python3-pip
RUN pip3 install selenium

RUN apt-get install wget
RUN wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip -P /tmp
RUN unzip /tmp/chromedriver_linux64.zip -d /tmp/

