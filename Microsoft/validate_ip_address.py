"""
Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. 
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, 
while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.


IPV4:
"x1.x2.x3.x4"
1. 0 <= xi <= 255

"192.168.1.0" valid
"192.168.1.00" invalid

IPV6:
"x1:x2:x3:x4:x5:x6:x7:x8"

1 <= xi.length <= 4
may contain (a, b, c, d, e, f) (A, B, C , D, E, F)
leading zeros are allowed

split(.)
172.16.254.1
   ^

split_addr = 
['172', '16', '254', '1']
  ^

may be a ipv4 addr

IPV4
for xi in split_addr:
    if not xi or not xi.has_digits() or xi.has_leading_zeros() or int(xi) < 0 or int(xi) > 255: return False
    return True

IPV6
for xi in split_addr:
    if not xi or len(xi) > 4 not xi.is_hex() or  


"""
import string
def is_hex(xi):
    for ch in xi:
        if xi not in string.hexdigits: return False
    return True

def is_ipv4(ip):
    X = ip.split('.')
    for xi in X:
        if not xi or not xi.isdigit() or (xi[0] == '0' and len(xi) != 1) or int(xi) < 0 or int(xi) > 255: return "Neither"
    return "IPV4"

def is_ipv6(ip):
    X = ip.split(':')
    for xi in X:
        if not xi or len(xi) > 4 or not is_hex(xi): return "Neither"
    
    return "IPV6"

from collections import Counter
def validate_ip(ip):
    cntr = Counter(ip)
    if cntr[':'] == 7:
        return is_ipv6(ip)
    
    elif cntr['.'] == 3:
        return is_ipv4(ip)
    
    else: return "Neither"