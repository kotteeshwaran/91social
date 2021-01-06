import os

def out(output):
    if '0 received' in output: 
        print('IP unreachable') 
    else: 
        print('Ip reachable')  
        recieve('Ip reachable') 

def recieve(reachable):
    if os.path.isfile("File.txt"):
        print("File exist")
    else:
        print("File not exist")
ipaddr = input('Enter the IP address:')
stream = os.popen('ping -c 4 {}'.format(ipaddr)) 
output = stream.read() 
out(output)

