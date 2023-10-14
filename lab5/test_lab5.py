import json
import re
import sys

regex = r"DEBUG: (.*) (.*)"
produced = []
consumed = []

with open(sys.argv[1], 'r') as infile:
    for line in infile:
        if re.search(regex, line): # start of message
            result = re.match(regex, line)
            if (result[2] == "produced"):
                produced.append(result[1])
            elif (result[2] == "consumed"):
                consumed.append(result[1])

produced.sort()
consumed.sort()

print(f"produced: {produced}")
print(f"consumed: {consumed}")

if produced == consumed:
    print(f"TEST PASSED")
else:
    print(f"TEST FAILED")
