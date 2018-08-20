#/usr/bin/bash
USER=root
PASSWD='123456'
HOST='192.168.4.50'
mysqldump -u$USER -p$PASSWD -h$HOST  -P3306 production_cmdb | gzip > /opt/mysqlbak/production_cmdb_`date '+%m-%d-%Y'`.sql.gz
## 解压命令  gunzip cmdb_04-26-2017.sql.gz###
## 还原备份 mysql -h192.168.4.20 -P3306 -ucmdb -pp@ssw0rd cmdb < cmdb_05-28-2017.sql  
