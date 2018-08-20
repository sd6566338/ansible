#/usr/bin/bash
USER=cmdb
PASSWD='p@ssw0rd'
HOST='192.168.4.20'
mysqldump -u$USER -p$PASSWD -h$HOST  -P3306 cmdb  cmdb_ticket| gzip > /opt/mysqlbak/cmdb_`date '+%m-%d-%Y'`.table.gz
## 解压命令  gunzip cmdb_04-26-2017.sql.gz###
## 还原备份 mysql -h192.168.4.20 -P3306 -ucmdb -pp@ssw0rd cmdb < cmdb_05-28-2017.sql  
