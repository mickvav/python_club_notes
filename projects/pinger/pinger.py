#!/usr/bin/env python3
import sys
import subprocess
import re


def ping(ip_address):
    ping_result = subprocess.run(['ping', '-c','4',ip_address],text=True, capture_output=True)
    print(ping_result.stdout)
    return(ping_result.stdout)

def parseping(s):
    
    match = re.search('(\d+) packets transmitted, (\d+) received, (\d+)% packet loss, time (\d+)ms', s)
    if match:
        match2 = re.search('([\d]*\.[\d]*)/([\d]*\.[\d]*)/([\d]*\.[\d]*)/([\d]*\.[\d]*)', s)
        if match2:
            if match.group(3) == '0':
                return ('1', match2.group(2))
            else:
                return('0', match2.group(2))
        else:
            return('0', "i don't know")
    else:
        return('0', 'no ping, check IP')

if __name__ == '__main__':
    ip_addresses = []
    with open('ip_list.txt', 'r') as f:
        for line in f:
            ip_addresses.append(line.strip())
        print(ip_addresses)
    ping_zero = ping(ip_addresses[2])
    print(parseping(ping_zero))
