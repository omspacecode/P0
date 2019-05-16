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
    calls_count = len(calls)

calls_within_blr = 0
all_calls_blr = 0
all_calls = 0
list_of_codes = set();

for call in calls:
    if call[0].find("(080)") != -1 and call[1].find("(080)") != -1:
        list_of_codes.add(call[1])
        calls_within_blr += 1
        all_calls_blr += 1
        all_calls += 1
    elif call[0].find("(080)") != -1 and call[1].find("(") != -1:
        list_of_codes.add(call[1])
        all_calls_blr += 1
        all_calls += 1
    elif call[0].find("(080)") != -1 and ( call[1][0] == "9" or call[1][0] == "8" or call[1][0] == "7" ):
        list_of_codes.add(call[1])
        all_calls_blr += 1
        all_calls += 1
    else:
        all_calls += 1

print("The numbers called by people in Bangalore have codes:")
for code in sorted(list_of_codes):
    if(code.find(")") != -1):
        pos = code.find(")")
        print(code[:pos+1])
    else:
        print(code[:4])

percentage = ('{0:.2f}%'.format(( float(calls_within_blr)/float(all_calls_blr)  * 100)))
print(percentage," percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
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
