import re
data = []
for i in range(int(input().strip())):
    data.append(input().strip())

for i in range(int(input().strip())):
    word = input().strip()
    matches_count = 0
    for e in data:
        matches = re.findall(r'\b'+word+r'\b', e)
        matches_count += len(matches)

    print(matches_count)
