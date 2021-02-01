#!/system/xbin/bash
time=$(date)
blue='\033[34;1m'
green='\033[32;1m'
red='\033[31;1m'
printf "%s\n\n\n$green$time\n\n\n"
printf "%s\n1. Get String File for User\n2. Get String File for Bot\n3. Install Kebutuhan\n4. Clear File$red\n00. Cancel\n\n\n"
read -p "????????? :" okl
$blue
if [ "$okl" = 1 ] ||  [ "$okl" = 01 ]
then
cd /data/data/com.termux/files/home || exit || exit
python -V
if [ ! -e string_session.py ]; then
    printf  "\nDownloading string_session.py\n";wget https://raw.githubusercontent.com/meareyou/lel_remake_UserBoto/x-sql-extended/string_session.py;printf "\nRunning script...\n";sleep 1;python3 string_session.py
else
    printf  "\nstring_session.py detected... \nrunning existing file\n";sleep 1;python3 string_session.py
fi
fi

if [ "$okl" = 2 ] ||  [ "$okl" = 02 ]
then
cd /data/data/com.termux/files/home || exit;python -V
if [ ! -e string_support_bot.py ]; then
    printf  "\nDownloading string_session.py\n";wget https://raw.githubusercontent.com/meareyou/lel_remake_UserBoto/x-sql-extended/string_support_bot.py;printf "\nRunning script...\n";sleep 1;python3 string_support_bot.py
else
    printf  "\nstring_support_bot.py detected... \nrunning existing file\n";sleep 1;python3 string_support_bot.py
fi
sleep 90
fi

if [ "$okl" = 3 ] ||  [ "$okl" = 03 ]
then
pkg install python -y;pip install telethon;pkg install wget -y;cd /data/data/com.termux/files/home || exit;wget https://raw.githubusercontent.com/meareyou/ezrequ/main/requirements.txt;pip install -r requirements.txt
clear
fi

if [ "$okl" = 4 ] ||  [ "$okl" = 04 ]
then
printf "Clearing not used files";sleep 2;cd /data/data/com.termux/files/home || exit;rm -rf requirements.txt;rm -rf string_session.py;rm -rf string_support_bot.py;clear;logout
fi

if [ "$okl" = 0 ] || [ "$okl" = 00 ]
then
cd /data/data/com.termux/files/home || exit;clear;logout
fi
clear
