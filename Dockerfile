FROM public.ecr.aws/lambda/python:3.8


COPY app.py ./

RUN pip3 install requests
RUN pip3 install beautifulsoup4
RUN pip3 install html5lib
RUN pip3 install selenium

RUN yum install wget -y
RUN yum install tar -y
RUN yum install gzip -y
# Gecko Driver
ENV GECKODRIVER_VERSION 0.29.0
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
  && rm -rf /opt/geckodriver \
  && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
  && rm /tmp/geckodriver.tar.gz \
  && mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \
  && chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \
  && ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver \
  && ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/wires

CMD [ "app.handler" ]