#coding=utf-8
import MySQLdb, os, datetime
##########定义全局变量##########
mysql_ip='192.168.4.20'
mysql_user='cmdb'
mysql_password='p@ssw0rd'
mysql_DB='cmdb'
password_ecc='Passw0rd@ilo'
##########连接数据库###########
conn= MySQLdb.connect(mysql_ip,mysql_user,mysql_password,mysql_DB)
cursor = conn.cursor()
stat = "0" ##初始化机器健康状态为“0”
sql_search_mod = "select manager_ip from cmdb_server where idc_mod = '%s'" %'Mod2' ##定义sql查询语句
cursor.execute(sql_search_mod) ##执行sql语句
ip_data = cursor.fetchall() ##获取ip地址信息
##########开始干活##########
for ip in ip_data:
    sql_find_password = "select password from cmdb_server where manager_ip='%s';" %ip[0]##定义获取password的sql语句
    cursor.execute(sql_find_password) ##执行sql语句
    password = cursor.fetchall() ##从数据库获取password信息
    ipmicmd = "ipmitool -I lanplus -H"+" "+ip[0]+" "+"-U admin -P %s  sdr" % password[0][0] ##定义ipmi命令
    output = os.popen(ipmicmd) ##执行ipmi
    res = output.read(100) ##获取结果的前100字符
    if '0x00' in res: ##判断res内是否包含服务器健康状态的关键代码
        stat = 1 ##如果有将stat设置为True
    else:
        stat = 0  ##如果没有将stat设置为False
    update_date = datetime.datetime.now() ##获取当前时间
    print update_date
    print  ip[0]
    print stat
    print password[0][0]
#    datetime.datetime.now()
    cursor.execute("update cmdb_server set health=%d, update_date='%s' where manager_ip='%s'" % (stat, update_date, ip[0]))   ##将获取的Health LED结果写入数据库；

cursor.close()
conn.commit()
conn.close()
