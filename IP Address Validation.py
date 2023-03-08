import re
for i in range(int(input().strip())):
    data = input().strip()
    match_ipv4 = re.search('^([0-9]|[01]?[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.([0-9]|[01]?[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$', data)
    match_ipv6 = re.search('^([0-9a-fA-F]{1,4})(:([0-9a-fA-F]{1,4})){7}$', data)

    if match_ipv4 == None and match_ipv6 != None:
        ip_ver = "IPv6"
    elif match_ipv4 != None and match_ipv6 == None:
        ip_ver = "IPv4"
    else:
        ip_ver = "Neither"

    print(ip_ver)
