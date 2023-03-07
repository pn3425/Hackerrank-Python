import re
domains = set()
for i in range(int(input().strip())):
    data = input().strip()
    matches = re.findall(r'https?:\/\/(?:ww[w2]\.)?(([A-Za-z0-9-]+\.)+([A-Za-z-]+))', data)
    if matches:
        for m in matches:
            domains.add(m[0].strip())

domain_list = list(domains)
domain_list.sort()

for i in range(len(domain_list)-1):
    print(domain_list[i] + ';', end="")

print(domain_list[i+1])
