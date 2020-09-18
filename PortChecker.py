#PORT CHECKER
import socket

#defining a list of ports to use 
PortName = ["HTTP", "HTTPS", "SSH", "FTP", "FTPs", "POP3","SMTP", "DNS"]
PortList = [80, 443 , 22 ,  20, 990, 110, 25, 53]
PortOpen = []

def isOpen(ip,port):
    #initiates an object to be used to stream data
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
       #connects object with your IP and the port you want to check
      s.connect((ip, int(port)))
      #shuts down the stream as it's not being used. 
      s.shutdown(2)
      return True
   except:
      return False

hostname = socket.gethostname()    
ip = socket.gethostbyname(hostname)
port = 80
loop = 0
for i in PortList:
    isOpen(ip,i)
    if True:
        
        PortOpen.append(loop)
    loop = loop+1 


print("These are the ports that are open: ")
for x in PortOpen:
    print(" - " + PortName[x])
    



