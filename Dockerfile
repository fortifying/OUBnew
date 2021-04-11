FROM heinzdf/oubnew:buster
 
# Clone repo and prepare working directory
RUN git clone -b sql-extended https://github.com/fortifying/OUBnew /OUBnew
RUN chmod 777 /OUBnew
WORKDIR /OUBnew
 
# Copies session and config (if it exists)
COPY ./sample_config.env ./userbot.session* ./config.env* /root/userbot/
 
# Install requirements
CMD ["python3","-m","userbot"]
