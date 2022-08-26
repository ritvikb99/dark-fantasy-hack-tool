from modules.clear_scr import clear_scr
from modules.dos import dos
from modules.scanner import scanner
from modules.ftp import ftp
from modules.banner import banner
from modules.spider import spider
from modules.email import email
from modules.subdomain_scanner import scan_subdomains


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
        print("1.Port Scanning\n2.DDOS\n3.Banner Grabbing\n4.Web spider(gather all URLs for web hacking)\n5.FTP Password Cracker\n6.Email Scraping\n7.Subdomain Scanner")
        try:
            choice = int(input("Enter Your Choice: "))
        except (ValueError, EOFError, KeyboardInterrupt):
            return print('\n[!] Interrupted! or Wrong Value')

        if choice not in range(8):
            return print('Invalid choice')

        hostname = ask_host()
        if choice == 1:
            scanner(hostname)
        elif choice == 2:
            dos(hostname)
        elif choice == 3:
            banner(hostname)
        elif choice == 4:
            spider(hostname)
        elif choice == 5:
            ftp(hostname)
        elif choice == 6:
            email(hostname)
        elif choice == 7:
            # Only accepts domain name such as example.com, ip address aren't valid input
            scan_subdomains(hostname)
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
