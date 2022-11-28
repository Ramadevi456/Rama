import os, ipaddress
'''import socket
#print(socket.gethostname())
import os
hostname = socket.gethostname()
print(hostname)
ipadd = socket.gethostbyname(hostname)
print(ipadd)
'''
os.system('cls')
while True:
    ip=input("enter ip address:")
    try:
        print(opaddress.ip_addtress(ip))
        print('ip valid')
    except:
        print('-'*50)
        print('it is not valid')
    finally:
        if ip=='q':
            print('Script Finished')
            break
