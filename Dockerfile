FROM public.ecr.aws/lambda/python:3.8


COPY app.py ./

RUN pip3 install requests
RUN pip3 install beautifulsoup4
RUN pip3 install html5lib


CMD [ "app.handler" ]