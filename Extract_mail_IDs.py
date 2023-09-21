import re

with open('mail.txt', 'r') as fh:
    data = fh.read()

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b'
result = re.findall(pattern, data)
for email in result:
    print(email)
