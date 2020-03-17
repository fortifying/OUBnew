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
# Clone repo and prepare working directory
#

RUN git clone 'https://github.com/fortifying/OUBnew' /root/userbot
RUN mkdir /root/userbot/bin/
RUN chmod 777 /root/userbot/
RUN chmod 777 /root/userbot/bin/

#
# Copies session and config (if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /root/userbot/

#
# Install requirements
#
RUN pip3 install -r requirements.txt
CMD ["python3","-m","userbot"]
