#! /usr/bin/env python3
import re
from dateutil import parser
from datetime import timedelta
from datetime import datetime

f = open('inputs/4','r')

events = {}
for x in f:
    _s = x.split("]")
    dt = _s[0][1:]
    dt = datetime.strptime(dt, "%Y-%m-%d %H:%M") 
    entry = _s[1][1:].rstrip()
    events[dt] = entry

total_counter = {}
guard = None
snorlax = None
_max = 0
sleeping = False
index = 0
sorted_keys = sorted(events)
curr_ts = sorted_keys[0]
print(curr_ts)
last_ts = sorted_keys[-1]
print(last_ts)
while curr_ts <= last_ts:
    if curr_ts in events:
        e = events[curr_ts]
        if e.startswith("Guard"):
            guard = e.split()[1][1:]
        elif e == "wakes up":
            sleeping = False
        elif e == "falls asleep":
            sleeping = True
    if curr_ts.hour == 00:
        if guard not in total_counter:
            total_counter[guard] = []
        if sleeping:
            total_counter[guard].append(curr_ts.minute)

        if len(total_counter[guard]) > _max:
            _max = len(total_counter[guard])
            snorlax = guard
    if curr_ts.hour == 1:
        curr_ts += timedelta(hours=22)
    else:
        curr_ts += timedelta(minutes=1)

print("guard",snorlax)
_max = 0
minute = 0
for x in range(0,60):
    if total_counter[snorlax].count(x) > _max:
        _max = total_counter[snorlax].count(x)
        minute = x
print("minute",minute)
