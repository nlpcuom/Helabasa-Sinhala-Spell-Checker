from multiprocessing.connection import Listener
from array import array

address = ('localhost', 25035)     # family is deduced to be 'AF_INET'

while(1):
	with Listener(address, authkey=b'123@kbs') as listener:
		with listener.accept() as conn:
			
			data = conn.recv()
			conn.send(data)
