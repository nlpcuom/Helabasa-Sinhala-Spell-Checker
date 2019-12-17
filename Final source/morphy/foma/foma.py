import sys
import subprocess

def process(cmd):
	
	try:

		process = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
		proc_stdout = process.communicate()[0].strip()
		
		
	
		return proc_stdout
		
	except Exception, e:

		print(e)

		
	
if __name__ == "__main__":
	print(process(sys.argv[1]))