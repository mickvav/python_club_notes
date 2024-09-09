#!/usr/bin/env python3
import subprocess
import re
import random
import ipaddress
import sys
from multiprocessing import Pool


def ping(ip_address):
    ping_result = subprocess.run(['ping', '-c','1',str(ip_address)],text=True, capture_output=True)
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
def readfile(filename):
    ip_addresses = []
    with open(filename, 'r') as f:
        for line in f:
            ip_addresses.append(line.strip())
        print(ip_addresses)
    return ip_addresses

def randomgeneratorip(networks,limit,file):
    random_ips = []
    for _ in range(limit):
        random_network = random.choice(ip_addresses)
        network = ipaddress.ip_network(random_network)
        all_ip = list(network.hosts())
        random_ip = random.choice(all_ip)
        #print(random_ip)
        random_ips.append(random_ip)
    print(random_ips)
    with Pool(limit) as p:
        results = p.map(ping, random_ips)
    for i in range(limit):
        newvar = parseping(results[i])
        print(parseping(str(results[i])))
        file.write(str(random_ips[i]) +" " + newvar[0] +" " + newvar[1] + "\n" )
    #return ping_zero
if __name__ == '__main__':
    ip_addresses = readfile(sys.argv[1])
    with open ('ping_result.txt', 'w') as f:
        results = randomgeneratorip(ip_addresses, int(sys.argv[2]),f)
    
    
