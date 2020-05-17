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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Used for pattern matching
import re 

# Filter for phones numbers with area code beginning with (080)
called_code_numbers = []
for call in calls:
    if '(080)' in call[0]:
        # Then Begin search for incoming numbers 
        match = re.search(r"\(\w+\)", call[1])
        if match:
            called_code_numbers.append(match.group())
        # finish with area codes and check all mobile numbers with no parentheses
        if re.search(r"^[7-9]", call[1]):
            match = re.search(r"[0-9]+", call[1])
            called_code_numbers.append(match.group())

print(f"The numbers called by people in Bangalore have codes:")
list_ = list(sorted(set(called_code_numbers)))
for elem in list_:
    print(elem)

# capture all calls from banglaore to any number, then capture calls only between Bangalore numbers 
total_calls = []
b_b_calls = [] 
for call in calls:
    if '(080)' in call[0]:
        total_calls.append([call[0], call[1]])
    if (('080') in call[0]) & (('080') in call[1]):
        b_b_calls.append([call[0], call[1]])

percent_calls = (len(b_b_calls)/(len(total_calls)))*100

print(f'{percent_calls:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore')