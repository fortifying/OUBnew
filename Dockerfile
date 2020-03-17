# We're using Ubuntu
FROM ubuntu:18.04

ENTRYPOINT ["mysql"]

#
# We have to uncomment Community repo for some packages
#
RUN apt-get update \

 && apt-get install -y --no-install-recommends mysql-client \
 && rm -rf /var/lib/apt/lists/*
#
#
RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/fortifying/OUBnew/ /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/

#
# Copies session and config (if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /root/userbot/

#
# Install requirements
#
RUN pip3 install -r requirements.txt
CMD ["python3","-m","userbot"]
