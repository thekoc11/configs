import telnetlib
from time import sleep
import socket

def telnt():
	
	tn = telnetlib.Telnet()
	print "808"
	
	try:
		
		tn.open("8.8.8.8", 23, 2)
	
	
	except socket.timeout:
		print "Signed in"
		pass
	
	else:
	
		tn.read_until("login: ", 1)

		tn.write("adityap17\n")

		tn.read_until("password: ", 1)

		tn.write("iiserb5857\n")

		tn.interact()

		tn.close()
	
	
if __name__ == '__main__':
	i = 0
	while True:
		telnt()
		print ("909 + " , i)
		sleep(10)
		i = i + 1
