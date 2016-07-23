import socket
import sys
import codecs

host = '0.0.0.0'
port = 8080

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
except socket.error as msg:
	print(msg)
	sys.exit()

s.listen(5)                     
print 'Server Up and Running'
while True:
	c, addr = s.accept()
	data = c.recv(2048)
	data = data.split()

	if (data[1]!='/DN.html'):
		c.send('HTTP/1.0 404 Not Found\n'+'Content-Type: text/html\n\n')
		c.send("""
		    <html>
		    <body>
		    <h1>404 Error</h1> Page not found<br><br><br>
		    <center>
		    THANK YOU MARIO!<br> BUT THE PAGE YOU ARE LOOKING FOR IS AT ANOTHER URL! :D
		    </center>
		    </body>
		    </html>
		""")
		c.close()
	else:
		f=codecs.open("DN.html", 'r')
		a = f.read()
		c.send('HTTP/1.0 200 OK\n'+'Content-Type: text/html\n\n'+a)
		c.close()                                                            
s.close()

