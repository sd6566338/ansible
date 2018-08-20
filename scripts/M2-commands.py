#/usr/bin/evn python
#coding=utf-8

from cmdb.models import Server



Lista = Server.objects.filter(cabinet_list='A')
for i in List_a:
    print i.sn

