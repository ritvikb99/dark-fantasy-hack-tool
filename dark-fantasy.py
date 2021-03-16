from modules.clear_scr import clear_scr
from modules.dos import dos
from modules.scanner import scanner
from modules.ftp import ftp
from modules.banner import banner
from modules.spider import spider
from modules.email import email


def ask_host():
    hostname = input(
        "Enter hostname or IP address (google.com, www.yoursite.com, 192.168.1.1): ")
    if '://' in hostname:
        hostname = hostname.split('://')[1]
    return hostname


def main():
    while 1:
        print("-" * 60 + "\n")
        print("                  Dark Fantasy - Hack Tool                    ")
        print("-" * 60 + "\n")
        print(
            "1.Port Scanning\n2.DDOS\n3.Banner Grabbing\n4.Web spider(gather all URLs for web hacking)\n5.FTP Password Cracker\n6.Email Scraping")
        try:
            choice = int(input("Enter Your Choice: "))
        except (ValueError, EOFError, KeyboardInterrupt):
            return print('\n[!] Interrupted! or Wrong Value')

        if choice not in range(7):
            return print('Invalid choice')

        hostname = ask_host()
        # Use a dict instead of several if-elses
        choices = {1: scanner(hostname),
                   6: email(hostname),
                   3: banner(hostname),
                   5: ftp(hostname),
                   2: dos(hostname),
                   4: spider(hostname)}
        # Raise an error if not in choices not print

        if choice not in choices:
            raise ValueError("You chose {} which is not valid".format(choice))

        choices[choice]


if __name__ == '__main__':
    main()

