import socket
from datetime import datetime
from modules.clear_scr import clear_scr


def scanner(host):
    clear_scr()

    t1 = datetime.now()
    socket.setdefaulttimeout(2)
    print("[*] Scanning "+host)
    print("[*] Starting Scanning at "+str(t1))
    host = socket.gethostbyname(host)
    print("[*] IP of host: "+host)
    ports = [1, 5, 7, 18, 20, 21, 22, 23, 25, 43, 42, 53, 80, 109,
             110, 115, 118, 443, 194, 161, 445, 156, 137, 139, 3306]
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
