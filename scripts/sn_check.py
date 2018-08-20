#coding=utf-8
import MySQLdb, os, datetime, re
mysql_ip='172.16.224.12'
mysql_user='root'
mysql_password='123456'
mysql_DB='production_cmdb'
#password_ecc='Passw0rd@ilo'
##########连接数据库###########
conn= MySQLdb.connect(mysql_ip,mysql_user,mysql_password,mysql_DB)
cursor = conn.cursor()
stat = "0"
sql_search_mod = "select manager_ip from cmdb_server where sn = '%s';" % 'sn'
cursor.execute(sql_search_mod)
ip_data = cursor.fetchall()
##########开始干活##########
for ip in ip_data:
    print  ip[0]
    sql_find_password = "select password from cmdb_server where manager_ip='%s';" % ip[0]
    cursor.execute(sql_find_password)
    password = cursor.fetchall()
    ipmicmd_get_ip = "ipmitool -I lanplus -H"+" "+ip[0]+" "+"-U admin -P %s  sdr" % password[0][0]
    ipmicmd_get_sn = "ipmitool -I lanplus -H"+" "+ip[0]+" "+"-U admin -P %s  fru list" % password[0][0]

    output_get_sn = os.popen(ipmicmd_get_sn)
    res_get_sn = output_get_sn.read(180)
    pattern_get_sn = re.compile('Chassis Serial\s+:\s*(\w+)')
    sn = re.findall(pattern_get_sn,res_get_sn)

    output_get_ip = os.popen(ipmicmd_get_ip)
    res_get_ip = output_get_ip.read(100)
    if '0x00' in res_get_ip:
        stat = 1
    else:
        stat = 0
    update_date = datetime.datetime.now()
    print update_date
    print  ip[0]
    print  sn[0]
    print stat
    print password[0][0]
#    datetime.datetime.now()
    cursor.execute("update cmdb_server set sn='%s', update_date='%s' where manager_ip='%s'" % (sn[0], update_date, ip[0]))   ##将获取的Health LED结果写入数据库；

cursor.close()
conn.commit()
conn.close()
