#!/usr/bin/python

'''
# coding: utf-8
# Scanner v0.1.0
# AUTHORS Meuz G - github.com/meuzgebre 
# EDITED FOR DARK FANTASY Ritvik Bhatia - github.com/ritvikb99
'''

# import the required module
import requests
from termcolor import colored
from modules.clear_scr import clear_scr
from pathlib import Path


def get_subdomains(text_file):
    '''
    This function is used to get the subdomains of a given text and return list of them
        params: text_file | file - a text file with list of domain names
        return: list of all the subdomains
    '''
    subdomains = []

    # Converting the file in to list of lines
    with open(text_file, 'r+') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            else:
                subdomains.append(line)

    # Return the list of subdomains
    return subdomains


def scan_subdomains(domain_name):
    '''
    This function is used to scan all the subdomains of a given text and return list of them
        params: subdomains | list - a list of subdomains
        params: domain_name | str - the domain name to scan for
        return: list of all the subdomains of a given domain name
    '''
    print(colored(f'[+] Subdomain Scanner', 'green'))
    try:
        ssl_enabled = int(
            input("(SSL)Do you want to check urls with which prefix \n1. http:// \n2. https:// \n"))
    except (ValueError, EOFError, KeyboardInterrupt):
        return print('\n[!] Interrupted! or Wrong Value')

    if ssl_enabled == 1:
        ssl_enabled = False
    elif ssl_enabled == 2:
        ssl_enabled = True
    else:
        return print("Invalid Choice")

    clear_scr()

    # Check doman name pattern matches
    sub_domains = get_subdomains('modules/subdomains.txt')
    subdomains_list = []    # list of all valid subdomains
    valid_subdomains = 0    # total number of subdomains found
    url_prefix = "https://" if ssl_enabled else "http://"

    # Check if subdomains is valid using requests
    print(colored('[+] Subdomain Scanner', 'green'))
    print("[+] Scanning for subdomains")
    print("[+] Program will return to main menu once scanning is complete")
    print("[+] You can press Ctrl+C to stop scanning")
    print("[+] Output Saved in subdomain_output.txt [same folder as software]")
    print("[+] If you want to use your list of subdomains. Please edit *dark_fantasy_folder*/modules/subdomains.txt\n")

    with Path("subdomain_output.txt").open('w') as out_file:
        try:
            for sub_domain in sub_domains:

                url = f'{url_prefix}{sub_domain}.{domain_name}'

                try:

                    # Sending get request to url
                    requests.get(url)

                    # if valid print url
                    print(colored(f'[+] {url}', 'blue'))

                    # add result to list
                    subdomains_list.append(url)

                    # add url to output file
                    out_file.write(url+'\n')

                    valid_subdomains += 1
                except requests.ConnectionError:
                    pass
        except KeyboardInterrupt:
            return print("You pressed Ctrl+C")

    return subdomains_list
