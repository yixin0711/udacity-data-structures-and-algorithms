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

tele_numbers = []
for i in range(len(texts)):
    tele_numbers.append(texts[i][0])
    tele_numbers.append(texts[i][1])
for i in range(len(calls)):
    tele_numbers.append(calls[i][0])
    tele_numbers.append(calls[i][1])

output = set(tele_numbers)
print("There are {} different telephone numbers in the records.".format(len(output)))