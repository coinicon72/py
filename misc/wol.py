import argparse
import re
from socket import socket, AF_INET, SOL_SOCKET, SOCK_DGRAM, SO_REUSEADDR, SO_BROADCAST

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

def sendWol(macstr, password):
    '''
    SEE:
    + https://en.wikipedia.org/wiki/Wake-on-LAN
    + https://wiki.wireshark.org/WakeOnLAN
    '''
    mac = [int(s, 16) for s in re.split(r'[:,-\.]', macstr)]
    data = [0xff] * 6 + mac * 16

    if password != None:
        pwd = [int(s, 16) for s in re.findall(r'\w{2}', password)]
        data += pwd
    
    data = bytearray(data)

    if password == None:
        print(f'sending wol package to {macstr} ...')
    else:
        print(f'sending wol package to {macstr} with password {password} ...')

    return cs.sendto(data, ('255.255.255.255', 9))

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(prog='wake-on-lan util')
    argparser.add_argument('mac', type = str, help = 'mac address of target machine, example: 44:87:fc:7a:3f:e3')
    argparser.add_argument('-p', dest='password', metavar = 'password', type = str, help='wol password, example: 123456789abc')

    args = argparser.parse_args()

    pwd = args.password
    if pwd != None:
        pwd = pwd.strip()

    if sendWol(args.mac, pwd) == 102:
        print('done')
    else:
        print('failed')