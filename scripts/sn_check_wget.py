#coding=utf-8
import MySQLdb, os, datetime, re
mysql_ip='192.168.4.20'
mysql_user='cmdb'
mysql_password='p@ssw0rd'
mysql_DB='cmdb'
#password_ecc='Passw0rd@ilo'
##########连接数据库###########
conn= MySQLdb.connect(mysql_ip,mysql_user,mysql_password,mysql_DB)
cursor = conn.cursor()
stat = "0"
sql_search_mod = "select manager_ip from cmdb_server where sn like '%s';" % '12%'
cursor.execute(sql_search_mod)
ip_data = cursor.fetchall()
##########开始干活##########
for ip in ip_data:
    print  ip[0]
    shell_get_sn="wget https://'%s' 2>&1" % ip[0]
    output_get_sn = os.popen(shell_get_sn)
    res_get_sn = output_get_sn.read()
    pattern_get_sn = re.compile('ILO(\w+)')
    sn = re.findall(pattern_get_sn,res_get_sn)
    update_date = datetime.datetime.now()
    datetime.datetime.now()
    print sn
    cursor.execute("update cmdb_server set sn='%s', update_date='%s' where manager_ip='%s'" % (sn[0], update_date, ip[0]))   ##将获取的Health LED结果写入数据库；

cursor.close()
conn.commit()
conn.close()
