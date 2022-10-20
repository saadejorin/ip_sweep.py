import os
import subprocess
import sys

def ip_sweep():
    ip = input("Enter the ip address in the format X.X.X.X: ")
    range1 = int(input("Enter the range1: "))
    range2 = int(input("Enter the range2: "))
    for i in range(range1, range2):
        ip_address = ip + str(i)
        response = os.system("ping -c 1 " + ip_address)
        if response == 0:
            print(ip_address, 'is up!')
            with open('up.txt', 'a') as f:
                f.write(ip_address + '\n')
        else:
            print(ip_address, 'is down!')
            with open('dead.txt', 'a') as f:
                f.write(ip_address + '\n')

ip_sweep()
