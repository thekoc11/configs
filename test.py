import telnetlib
from time import sleep
import socket
import sys

def telnt():
	
	
	#print "808"
	
	try:
		tn = telnetlib.Telnet("8.8.8.8", 23, 2)
	
	
	except socket.timeout:
		#print "Signed in"
		sys.exit(1)
		pass
	
	else:
	
		tn.read_until("login: ", 1)

		tn.write("adityap17\n")

		tn.read_until("password: ", 1)

		tn.write("iiserb5857\n")

		try:
			tn.interact()
		except:
			sys.exit(0)
			pass

		tn.close()
		
		
	
	
if __name__ == '__main__':
	i = 0
	telnt()



