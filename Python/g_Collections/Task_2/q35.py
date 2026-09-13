blocked_ips = {
    "192.168.1.100",
    "203.0.113.5",
    "198.51.100.42",
    "2001:db8::1"
}
print(blocked_ips)
new_blocked = input("Enter newly blocked IPs: ")
blocked_ips.add(new_blocked)
print(blocked_ips)
trusted = input("Enter trusted IPs to unblock: ")
blocked_ips.remove(trusted)
print(blocked_ips)