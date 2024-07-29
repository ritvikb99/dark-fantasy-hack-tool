# Written by SniverDaBest
import dns.resolver
import dns.reversename

def ip_to_domain(ip):
    try:
        addr = dns.reversename.from_address(ip)
        resolved = dns.resolver.resolve(addr, "PTR")
        result = [str(rdata) for rdata in resolved]
    except Exception as e:
        return None
    
    if result:
        print("Reverse IP Lookup Result:")
        for hostname in result:
            hostname = list(hostname)
            if hostname[len(hostname)-1] == ".":
                hostname.pop(len(hostname)-1)
            hostname = ''.join(hostname)
            print(hostname)
    else:
        print("Failed to retrieve data.")
