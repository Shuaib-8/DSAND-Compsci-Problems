"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# To get a unique set of observations from containers - use the built-in data structure set() 

unique_telephone_numbers = set() 

texts_add_1 = [unique_telephone_numbers.add(texts[i][0]) for i in range(len(texts))]
texts_add_2 = [unique_telephone_numbers.add(texts[i][1]) for i in range(len(texts))]
calls_add_1 = [unique_telephone_numbers.add(calls[i][0]) for i in range(len(calls))]
calls_add_2 = [unique_telephone_numbers.add(calls[i][1]) for i in range(len(calls))]

print(f"There are {len(unique_telephone_numbers)} different telephone numbers in the records.")
