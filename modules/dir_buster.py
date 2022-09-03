#!/usr/bin/python

'''
# coding: utf-8
# Scanner v0.1.0
# AUTHORS Meuz G - github.com/meuzgebre
# EDITED FOR DARK FANTASY Ritvik Bhatia - github.com/ritvikb99
'''

# import the required module
from pathlib import Path
from termcolor import colored
import requests
from modules.clear_scr import clear_scr


# from termcolor import colored


def get_wordlist(text_file):
    '''
    This function is used to get the names inside wordlist and return list of them
        params: text_file | file - a text file with list of domain names
        return: list of all the subdomains
    '''
    names = []

    # Converting the file in to list of lines
    with open(text_file, 'r+') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            else:
                names.append(line)

    # Return the list of names
    return names


def scan_urls(domain_name):
    '''
    This function is used to scan a url and return if it is a valid url
        params: domain_name | str - the domain name to scan for
        return: list of all the valid urls
    '''

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

    url_prefix = "https://" if ssl_enabled else "http://"

    print("[+] Program will return to main menu once bruteforcing is complete")
    print("[+] You can press Ctrl+C to stop scanning")
    print("[+] Output Saved in dirbuster_output.txt [same folder as software]")
    print("[+] If you want to use your list of directories. Please edit *dark_fantasy_folder*/modules/wordlist.txt\n")
    print('[+] Brutforcing Started')

    # Check doman name pattern matches

    paths = get_wordlist('modules/wordlist.txt')
    url_list = []    # list of all valid urls
    valid_url = 0    # total number of valid urls found

    # Check if url is valid using requests

    with Path("dirbuster_output.txt").open('w') as out_file:
        try:
            for path in paths:

                url = f'{url_prefix}{domain_name}/{path}'

                try:

                    # Sending get request to url
                    response = requests.get(url)

                    # if valid print url
                    if response.status_code == 200:
                        print(colored(f'[+] {url}', 'blue'))

                        # add result to list
                        url_list.append(url)

                        # add url to output file
                        out_file.write(url+'\n')

                        valid_url += 1
                except requests.ConnectionError:
                    pass
        except KeyboardInterrupt:
            return print("You pressed Ctrl+C")

    return url_list
