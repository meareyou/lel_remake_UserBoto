# We're using Ubuntu 20.10
FROM xnewbie/remix:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b x-sql-extended https://github.com/meareyou/lel_remake_UserBoto /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/meareyou/lel_remake_UserBoto/x-sql-extended/requirements.txt

CMD ["python3","-m","userbot"]
