#!/usr/evn python
#coding=utf-8
import os, datetime, re, MySQLdb
mysql_ip='192.168.4.50'
mysql_user='root'
mysql_password='123456'
mysql_DB='production_cmdb'
#password_ilo='Huawei12#$'
##########连接数据库###########
conn= MySQLdb.connect(mysql_ip,mysql_user,mysql_password,mysql_DB)
cursor = conn.cursor()
#sql_search_mod = "select manager_ip from cmdb_server where sn is null;"
sql_search_mod = "select manager_ip from cmdb_server where sn='hpsn';"
cursor.execute(sql_search_mod)
ip_data = cursor.fetchall()
##########开始干活##########
for ip in ip_data:
    print  ip[0]

    ipmicmd_get_sn = "ipmitool -I lanplus -H '%s' -U admin -P 'password'  fru list" % ip
    output_get_sn = os.popen(ipmicmd_get_sn)
    res_get_sn = output_get_sn.read()
    print res_get_sn
    pattern_get_sn = re.compile('Product Serial\s+:\s*(\w+)')
    sn = re.findall(pattern_get_sn,res_get_sn)
    update_date = datetime.datetime.now()
    datetime.datetime.now()
    print sn
    cursor.execute("update cmdb_server set sn='%s' where manager_ip='%s';" % (sn[0], ip[0]))

cursor.close()
conn.commit()
conn.close()

