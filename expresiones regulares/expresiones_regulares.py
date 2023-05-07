#!/usr/bin/python3
#1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland,FALSE
#Buscar los partidos amistosos en los que empataron de manera goleadora

import re

pattern = re.compile(r'^(\d{4}\-\d{2}\-\d{2}),(.+),(.+),(\d+),(\d+),Friendly,.*$')

empates_amistosos = 0
no_empates_amistosos = 0
total = 0

f = open("./results.csv", "r")

for line in f:
    res = re.match(pattern, line)
    if res:
        if (res.group(4) == res.group(5)) and ((int(res.group(4)) + int(res.group(5))) > 8):
            print(f"{res.group(1)}: {res.group(2)} {res.group(4)} - {res.group(3)} {res.group(5)}")
            empates_amistosos+=1
        else:
            no_empates_amistosos+=1
    else:
        no_empates_amistosos+=1
    total+=1

f.close()

print(f"Empates amistosos goleadores: {empates_amistosos}, no empates amistosos goleadores: {no_empates_amistosos}")
print(f"Total contados: {total}, total suma: {empates_amistosos + no_empates_amistosos}")
