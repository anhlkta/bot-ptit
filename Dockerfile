FROM python:3.10-alpine

WORKDIR /bot_code

COPY ["bot", "./bot"]

WORKDIR /bot_code/bot

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]

