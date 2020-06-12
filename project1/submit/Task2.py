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

durations = {}

for caller, receiver, time, duration in calls:
    if caller in durations.keys():
        durations[caller] += int(duration)
    else:
        durations.update({caller: int(duration)})
    if receiver in durations.keys():
        durations[receiver] += int(duration)
    else:
        durations.update({receiver: int(duration)})

longest_key = max(durations, key = durations.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_key, durations[longest_key]))