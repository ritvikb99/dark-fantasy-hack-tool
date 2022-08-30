#!/usr/bin/python

'''
# coding: utf-8
# Scanner v0.1.0
# AUTHORS Meuz G - github.com/meuzgebre
'''

# import the required module
import requests
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

    # Check doman name pattern matches

    paths = get_wordlist('wordlist.txt')
    url_list = []    # list of all valid urls
    valid_url = 0    # total number of valid urls found

    # Check if url is valid using requests

    for path in paths:

        url = f'https://{domain_name}/{path}'

        try:

            print ('############################## Scanning Starts ##############################')
            # Sending get request to url
            response = requests.get(url)

            # if valid print url
            if response.status_code == 200:
                print (f'[+] {url}')

                # add result to list
                url_list.append(url)

                valid_url += 1
        except requests.ConnectionError:
            pass

    return url_list

if __name__ == '__main__':
    scan_urls('python.org')