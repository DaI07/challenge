import re

text = "The ghost that says boo haunts the loo"

print(text)

matches = re.findall(".oo", text)
for match in matches:
    print(match)
