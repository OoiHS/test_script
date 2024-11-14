<start>
import subprocess

command = "mkdir testdir"
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()
#print( output )
#print( error )
<end>
