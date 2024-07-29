# Written by SniverDaBest
import dns.resolver

def domain_to_ip(host):
    try:
        result = dns.resolver.resolve(host, 'A')
        ips = [str(ip) for ip in result]
    except Exception as e:
        return None
    
    if ips:
        print(f"IP addresses of {host}:")
        for ip in ips:
            print(ip)
    else:
        print("Failed to retrieve IP addresses.")
