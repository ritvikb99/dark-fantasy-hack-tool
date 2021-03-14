import socket
from modules.clear_scr import clear_scr


def banner(host):
    clear_scr()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        "Error"
    host = socket.gethostbyname(host)
    port = int(input("[*] Enter the port of the service: "))
    try:
        s.connect((host, port))
        print("[*] connection successfull\nWaiting for the banner...\n")
        if port == 80:
            msg = 'HEAD / HTTP/1.0\r\n\r\n'
            msg = msg.encode()
            s.send(msg)
        data = s.recv(1024)
        print("Banner:\n"+data.decode())

        s.close()
    except Exception as e:
        print(e)
