#!/usr/bin/python

'''
# coding: utf-8
# Scanner v0.1.0
# AUTHORS Meuz G - github.com/meuzgebre
'''

# import the required module
import requests
from termcolor import colored

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

    # Check doman name pattern matches

    sub_domains = get_subdomains('modules/subdomains.txt')
    subdomains_list = []    # list of all valis subdomains
    valid_subdomains = 0    # total number of subdomains found

    # Check if subdomains is valid using requests

    for sub_domain in sub_domains:

        url = f'https://{sub_domain}.{domain_name}'

        try:

            # Sending get request to url
            requests.get(url)

            # if valid print url
            print (colored(f'[+] {url}', 'blue'))

            # add result to list
            subdomains_list.append(url)

            valid_subdomains += 1
        except requests.ConnectionError:
            pass

    return subdomains_list
