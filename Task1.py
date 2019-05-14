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

tel_numbers = set()

for text in texts:
	tel_numbers.add(text[0])
	tel_numbers.add(text[1])
for call in calls:
	tel_numbers.add(call[0])
	tel_numbers.add(call[1])

total_unique_tel_numbers = len(tel_numbers)
print("There are ",total_unique_tel_numbers ," different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
