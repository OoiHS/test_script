import subprocess
import time

while True:
  command = "mkdir testdir"
  process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  output, error = process.communicate()
  time.sleep(1)
  #print( output )
  #print( error )
