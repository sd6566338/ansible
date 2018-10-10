#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb,datetime

today = datetime.datetime.now().strftime('%Y-%m-%d')
db = MySQLdb.connect("localhost", "root", "123456", "newdb")

cursor = db.cursor()

sql="SELECT duty_day from cmdb_calendar where datelist='%s';" % today
cursor.execute(sql)
duty_day = cursor.fetchone()

sql="SELECT duty_night from cmdb_calendar where datelist='%s';" % today
cursor.execute(sql)
duty_night =  cursor.fetchone()

print duty_day[0],duty_night

db.close()

