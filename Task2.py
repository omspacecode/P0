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

max_time = 0
all_records = {}
for call in calls:
    all_records[call[0]] = 0
    all_records[call[1]] = 0

for call_rec in all_records:
    for call in calls:
        if call_rec == call[0]:
            tmp = all_records[call_rec]
            all_records[call_rec] = int(tmp) + int(call[3])
        if call_rec == call[1]:
            tmp = all_records[call_rec]
            all_records[call_rec] = int(tmp) + int(call[3])


maximum = max(all_records, key=all_records.get)
print (maximum,"spent the longest time, ",all_records[maximum]," seconds, on the phone during September 2016")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
