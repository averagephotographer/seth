from socket import socket, AF_INET, SOCK_STREAM
from time import time
from sys import stdout

DEBUG = False

# set timings for bits
ZERO = 0.025
ONE = 0.1


# declare ip and port to connect to
ip = "138.47.99.64"
port = 31337

# initialize the socket
s = socket(AF_INET, SOCK_STREAM)

# connect to server
s.connect((ip, port))

# recieve data from server
data = s.recv(4096).decode()

cov_bin = ""
# print data until EOF is recieved
while ((data.rstrip("\n")) != "EOF"):
	stdout.write(data)
	stdout.flush()
	
	t0 = time()
	data = s.recv(4096).decode()
	t1 = time()
	
	delta = round(t1 - t0, 3)
	
	if DEBUG:
		stdout.write(f" {delta}\n")
		stdout.flush
		
	if delta >= ONE:
		cov_bin += "1"
	else:
		cov_bin += "0"

# close connection to server
s.close()


covert = ""
i = 0
while (i < len(cov_bin)):
	b = cov_bin[i:i+8]
	try:
		covert += chr(int(f"0b{b}", 2))
	except:
		covert += "?"
	i += 8

print(covert)

