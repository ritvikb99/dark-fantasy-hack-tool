from pathlib import Path
from html2text import html2text
from modules.spider import spider
from modules.clear_scr import clear_scr
import urllib.request


def email(host):
    clear_scr()

    depth = spider(host)
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
                    cont = html2text(e.read().decode())
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
                    line = str(line)
                    if '@' in line:
                        print(line)
                        emails.write(line+"\n")

                count += 1
