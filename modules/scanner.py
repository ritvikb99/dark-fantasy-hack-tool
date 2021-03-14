import socket
from datetime import datetime
from modules.clear_scr import clear_scr


def scanner(host):
    clear_scr()
    print("Choose the type of scan:")
    print("1. Full Port Scan(1-65535) \n2. Specific port range\n3. Single Port \n4. Most popular ports")
    type_of_scan = int(input("Enter Your Choice: "))
    if type_of_scan == 1:
        ports = list(range(1, 65535))
    elif type_of_scan == 2:
        port1 = int(input("Enter starting port: "))
        port2 = int(input("Enter ending port: "))
        port2 += 1
        ports = list(range(port1, port2))
    elif type_of_scan == 3:
        ports = []
        ports.append(int(input("Enter the port to scan: ")))
    elif type_of_scan == 4:
        ports = [1, 5, 7, 18, 20, 21, 22, 23, 25, 43, 42, 53, 80, 109,
                 110, 115, 118, 443, 194, 161, 445, 156, 137, 139, 3306]
    else:
        print("[*] Wrong choice entered!")
        input()
        return
    clear_scr()
    t1 = datetime.now()
    socket.setdefaulttimeout(2)
    print("[*] Scanning "+host)
    print("[*] Starting Scanning at "+str(t1))
    host = socket.gethostbyname(host)
    print("[*] IP of host: "+host)

    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                print("Port {}: \t Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        return print("You pressed Ctrl+C")
    except socket.gaierror:
        return print('Hostname could not be resolved. Exiting')
    except socket.error:
        return print("Couldn't connect to server")

    t2 = datetime.now()
    timetaken = t2-t1
    print("[*] Scanning ended at: "+str(t2)+"\n")
    print("[*] Time taken= "+str(timetaken))
