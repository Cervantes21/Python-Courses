#!/usr/bin/python

import re

pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.*),Friendly,.*$')

f = open("./results.csv","r")

for line in f:
    res = re.match(pattern, line)
    if res:
        total = int(res.group(4)) + int(res.group(5))

        if total > 20:
            goals = res.goup(3).replace(res.group(3), "Brazil")
            print("goles: %s, %s %s - %s[%d-%d]"%total,res.group(1),res.group(2),goals,int(res.group(4)),int(res.group(5)))
f.close()

