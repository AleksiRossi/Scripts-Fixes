#!/bin/bash
LOGFILE=/home/oracle/transfer.log
ZIPFILE=/home/oracle/*.zip
echo "$(date "+%m%d%Y %T") : starting file transfer" >> $LOGFILE 2>&1
sftp "user"@"server":"filepath" >> $LOGFILE 2>&1
echo "$(date "+%m%d%Y %T") : transfer complete, starting unzip" >> $LOGFILE 2>&1
unzip -o $ZIPFILE >> $LOGFILE 2>&1
echo "$(date "+%m%d%Y %T") : unzip complete, starting import" >> $LOGFILE 2>&1
impdp dpump_user/"password" directory=dumpdir dumpfile="dumpfile" logfile=imp.log tables="user.table" table_exists_action=replace >> $LOGFILE 2>&1
echo -e "$(date "+%m%d%Y %T") : import complete \n" >> $LOGFILE 2>&1
