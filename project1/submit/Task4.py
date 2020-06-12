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

numbers = set()
for text in texts:
    numbers.add(text[0])    #sending text
    numbers.add(text[1])    #receiving text

call_numbers = set()
for call in calls:
    call_numbers.add(call[0])   #call
    numbers.add(call[1])        #receiving calls

#this set gives telephone numbers that in outgoing calls but nowhere else
possible_telemakers = sorted(call_numbers - numbers)
print("These numbers could be telemarketers: ")
for num in possible_telemakers:
    print(num)