# We're using ArchLinux
FROM dasbastard/arch:latest
 
#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/fortifying/OUBnew /home/OUBnew/
RUN pip3 install -r requirements.txt
RUN pip3 install pynewthonmath
RUN mkdir /home/OUBnew/bin/
WORKDIR /home/OUBnew/
CMD ["python3","-m","userbot"]
