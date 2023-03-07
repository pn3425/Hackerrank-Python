import re
emails = set()
for i in range(int(input().strip())):
    data = input().strip()
    matches = re.findall(r'([A-Za-z0-9_.]+@[A-Za-z0-9]+(?:\.[A-Za-z]+)*)', data)
    if matches:
        for m in matches:
            emails.add(m.strip())

email_list = list(emails)
email_list.sort()

for i in range(len(email_list)-1):
    print(email_list[i] + ';', end="")

print(email_list[i+1]
