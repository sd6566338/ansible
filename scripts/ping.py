#!/usr/bin/env python
import os,re
ip='10.214.255.2'
res=os.popen('ping'+' '+ ip +' '+'-c 1').read()
pattern_get_delay = re.compile('time=(\d+)\..+')
delay = re.findall(pattern_get_delay,res)
delay=int(delay[0])
