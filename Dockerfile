FROM ubuntu:20.04

RUN apt update
RUN apt-get install -y python-dev python3-distutils python3.8-dev python-dev python3-pip
RUN apt update

WORKDIR /bot_code

COPY ["bot", "./bot"]

WORKDIR /bot_code/bot

RUN pip3 install -r requirements.txt

CMD ["python3","bot.py"]

