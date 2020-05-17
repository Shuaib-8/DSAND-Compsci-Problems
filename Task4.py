"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = []
incoming_calls = []
send_texts = [] 
receive_texts = []

for incoming in calls:
    incoming_calls.append(incoming[1])
incoming_calls = set(incoming_calls)

for send in texts:
    send_texts.append(send[0])
send_texts = set(send_texts)

for receive in texts:
    receive_texts.append(receive[1])
receive_texts = set(receive_texts)

# Now we're able to find set of marketers starting from outgoing 140 calls
for call in calls:
    caller = call[0]
    if re.search(r"^(140)", caller):
        telemarketers.append(caller)
    # Next conditional that checks numbers that do not send (texts), receive (texts/calls) following from outgoing calls
    if not (caller in incoming_calls or caller in send_texts or caller in receive_texts):
        telemarketers.append(caller)

telemarketers = sorted(set(telemarketers))

print(f"These numbers could be telemarketers:")
for elem in telemarketers:
    print(elem)
