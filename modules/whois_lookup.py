import whois


def whois_lookup(host):
    i = 1
    w = whois.whois(host)

    #print(w)

    if type(w.get("domain_name")) is list:
        print("Domain name: " + str(w.get("domain_name")[0]).lower())
    elif type(w.get("domain_name")) is not list:
        print("Domain name: " + str(w.get("domain_name")).lower())
        
    print("Registrar: " + w.get("registrar"))
    print("Whois Server: " + w.get("whois_server"))
    if type(w.get("updated_date")) is list:
        for date in w.get("updated_date"):
            print("Last Updated: " + str(date))
    else:
        print("Last Updated: " + str(w.get("updated_date")))

    if type(w.get("creation_date")) is list:
        for date in w.get("creation_date"):
            print("Domain Created: " + str(date))
    else:
        print("Domain Created: " + str(w.get("creation_date")))
        
    if type(w.get("expiration_date")) is list:
        for date in w.get("expiration_date"):
            print("Domain Expires: " + str(date))
    else:
        print("Domain Expires: " + str(w.get("expiration_date")))

    for nameserver in w.get("name_servers"):
        print("Name server " + str(i) + ": " + nameserver)
        i = i + 1

    for status in w.get("status"):
        print("Status: " + str(status).split()[0])

    if type(w.get("emails")) is list: 
        for email in w.get("emails"):
            print("Email: " + email)
    else:
        print("Email: " + str(w.get("email")))
        
    print("DNSSEC: " + str(w.get("dnssec")))
    print("\nName: " + str(w.get("name")))
    print("Organization: " + str(w.get("org")))
    print("Address:\n" + str(w.get("address")) + "\n" + str(w.get("city")) + " " + str(w.get("state")))
    print(str(w.get("registrant_postal_code")))
    print(str(w.get("country")))
    
    
        
        
whois_lookup("stackoverflow.com")




