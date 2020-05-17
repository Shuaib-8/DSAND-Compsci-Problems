"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Built-in library to parse dates that are handled as string originally
# output as DD-MM-YY HH:MIN:S
from datetime import datetime
# Use defaultdict because there looks to be missing/null values for some observations which a normal dict() 
# cannot handle
from collections import defaultdict

calls_dict = defaultdict(int)

for outgoing, incoming, timestamp, duration in calls:
    date = datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
    # use int given we're handling duration (time)
    calls_dict[outgoing] += int(duration)
    calls_dict[incoming] += int(duration)

print(f'{max(calls_dict, key=calls_dict.get)} spent the longest time, {max(calls_dict.values())} seconds, \
on the phone during September 2016')
