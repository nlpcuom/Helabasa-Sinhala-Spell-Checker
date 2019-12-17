import base64
import sys
import json
from urllib.parse import unquote

from pyfasttext import FastText

from itertools import permutations

import hashlib

import datetime
from multiprocessing.connection import Client
from array import array


if __name__ == "__main__":

	word=sys.argv[1].encode('unicode_escape').decode('utf-8')
	word = json.loads(r'"'+word+'"')

	word=unquote(word)
	
	address = ('localhost', 25035)

	with Client(address, authkey=b'123@kbs') as conn:
		conn.send(word)
		array = conn.recv()
		print(array)
