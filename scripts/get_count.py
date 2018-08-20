#coding=utf-8
import MySQLdb, os, datetime
##########定义全局变量##########
mysql_ip='192.168.4.50'
mysql_user='root'
mysql_password='123456'
mysql_DB='cmdb'
##########连接数据库###########
conn= MySQLdb.connect(mysql_ip,mysql_user,mysql_password,mysql_DB)
cursor = conn.cursor()
sql_getcount = "select  cabinet_list,count(sn)  from cmdb_server group by cabinet_list;"
cursor.execute(sql_getcount) ##执行sql语句
#data = cursor.fetchall() ##获取ip地址信息
cabinet_list = [row[0] for row in cursor.fetchall()]
cursor.execute(sql_getcount)
server_count = [row[1] for row in cursor.fetchall()]
conn.close()
return render_to_response('base.html', {'cabinet_list': cabinet_list})
return render_to_response('base.html', {'server_count': server_count})
