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
max_time_record = []
for call in calls:
	if(int(call[3]) > max_time):
		max_time = int(call[3])
		max_time_record.clear()
		max_time_record.append(call[0])
		max_time_record.append(int(call[3]))

print(max_time_record[0],"spent the longest time, ",max_time_record[1]," seconds, on the phone during September 2016")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

