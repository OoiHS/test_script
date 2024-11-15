[start]import subprocess[end]

[start]command = "mkdir testdir"[end]
[start]process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)[end]
[start]output, error = process.communicate()[end]
[start]#print( output )[end]
[start]#print( error )[end]

