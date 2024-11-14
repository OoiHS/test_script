import os

try:
  os.system("mkdir testdir")
except Exception as e:
  print("fail")
