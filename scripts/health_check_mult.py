#coding=utf-8
import MySQLdb, os, threading, datetime
from time import ctime, sleep

##########
mysql_ip='192.168.4.20'
mysql_user='cmdb'
mysql_password='p@ssw0rd'
mysql_DB='cmdb'
##########

def mod2_checkA():
    conn= MySQLdb.connect(mysql_ip,mysql_user,mysql_password,mysql_DB)
    cursor = conn.cursor()
    stat = ""
    sql = "select manager_ip from cmdb_server where  cabinet_number = '%s';" %'04'
    cursor.execute(sql)
    ip_data = cursor.fetchall()
    for ip in ip_data:
        sql_find_password = "select password from cmdb_server where manager_ip='%s';" %ip[0]
        cursor.execute(sql_find_password) 
        password = cursor.fetchall()
        ipmicmd = "ipmitool -I lanplus -H"+" "+ip[0]+" "+"-U admin -P %s  sdr" % password[0][0]
        output = os.popen(ipmicmd)
        res = output.read(100)
        if '0x00' in res:
            stat = 1
        else:
            stat = 0   
        update_date = datetime.datetime.now()
        print update_date
        print  ip[0]
        print stat
        print password[0][0]
    #    datetime.datetime.now()
        cursor.execute("update cmdb_server set health=%d, update_date='%s' where manager_ip='%s'" % (stat, update_date, ip[0]))   ##将获取的Health LED结果写入数据库；
    
    
    cursor.close()
    conn.commit()
    conn.close()



def mod2_checkB():
    conn= MySQLdb.connect(mysql_ip,mysql_user,mysql_password,mysql_DB)
    cursor = conn.cursor()
    stat = ""
    sql = "select manager_ip from cmdb_server where  cabinet_number = '%s';" %'05'
    cursor.execute(sql)
    ip_data = cursor.fetchall()
    for ip in ip_data:
        sql_find_password = "select password from cmdb_server where manager_ip='%s';" %ip[0]
        cursor.execute(sql_find_password) 
        password = cursor.fetchall()
        ipmicmd = "ipmitool -I lanplus -H"+" "+ip[0]+" "+"-U admin -P %s  sdr" % password[0][0]
        output = os.popen(ipmicmd)
        res = output.read(100)
        if '0x00' in res:
            stat = 1
        else:
            stat = 0   
        update_date = datetime.datetime.now()
        print update_date
        print  ip[0]
        print stat
        print password[0][0]
    #    datetime.datetime.now()
        cursor.execute("update cmdb_server set health=%d, update_date='%s' where manager_ip='%s'" % (stat, update_date, ip[0]))   ##将获取的Health LED结果写入数据库；
    
    
    cursor.close()
    conn.commit()
    conn.close()

threads = []
t1 = threading.Thread(target=mod2_checkA)
threads.append(t1)
t2 = threading.Thread(target=mod2_checkB)
threads.append(t2)

if __name__=='__main__':

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print "over at %s"  %ctime()
