# Using Arch Linux
FROM anggarsx/arch:bleeding

#
# Clone repo and prepare working directory
#
RUN git clone 'https://github.com/fortifying/OUBnew' /root/userbot
RUN mkdir /root/userbot/bin/
RUN chmod 777 /root/userbot/
RUN chmod 777 /root/userbot/bin/
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
