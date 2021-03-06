FROM python:3.8-slim-buster

WORKDIR /app

COPY main.py main.py

RUN pip3 install requests
RUN pip3 install beautifulsoup4
RUN pip3 install html5lib

CMD ["python3", "main.py"]