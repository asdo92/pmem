#!/usr/bin/env python3

# -----------------------------------------------------------
# pmem - Show system memory                                 |
# Created by asdo92 (asdo92@duck.com)                       |
# Licensed by GPL v2.0                                      |
# Last update: 29-10-2022                                   |
# Compatible with Python 3.x                                |
# -----------------------------------------------------------
version="0.1"

# Import python-modules
import psutil
import os
import sys

# Check if your system use Python 3.x
if sys.version_info<(3,0):
  print ("")
  print (" You need python 3.x to run this program.")
  print ("")
  exit()

# Check system 
if os.name == "posix":
  os.chdir(os.environ["HOME"])
elif os.name == "nt":
  print("")
  print(" Error: Only Linux and *BSD systems are supported")
  print("")
  exit()

print('')
print(' List of processes (Mem + Name)')
print(' ==============================')
print('')

numprocess=0
for process in psutil.process_iter():
  numprocess = numprocess + 1
  Name = process.name() # Name of the process
  ID = process.pid # ID of the process
  readmemprocess = psutil.Process(ID)
  sysmemprocess = readmemprocess.memory_info()[0]
  ID = str(ID)
  if sysmemprocess > 1024:
    sysmemprocess = sysmemprocess / 1024
    sysmemprocess = round(sysmemprocess, 2)
    showmemprocess = str(sysmemprocess)
    showmemprocess = showmemprocess + ' KiB'
  if sysmemprocess > 1024:
    sysmemprocess = sysmemprocess / 1024
    sysmemprocess = round(sysmemprocess, 2)
    showmemprocess = str(sysmemprocess)
    showmemprocess = showmemprocess + ' MiB'
  if sysmemprocess > 1024:
    sysmemprocess = sysmemprocess / 1024
    sysmemprocess = round(sysmemprocess, 2)
    showmemprocess = str(sysmemprocess)
    showmemprocess = showmemprocess + ' GiB'
  print ('  ' + showmemprocess + '     ' + Name + ' (PID: ' + ID + ')')

# Read file /proc/meminfo and create variables
memfile = open('/proc/meminfo', 'r')
memread = memfile.read()
memsplit = memread.split()

# Memory variables
memtotal = memsplit[1]
memavailable = memsplit[7]

# Convert and calcule memory
memtotal = int(memtotal)
memavailable = int(memavailable)
memactive = memtotal - memavailable
if memsplit[2] == "kB":
  memtotal = memtotal / 1024 / 1024
  memavailable = memavailable / 1024 / 1024
  memactive = memactive / 1024 / 1024
elif memsplit[2] == "B":
  memtotal = memtotal / 1024 / 1024 / 1024
  memavailable = memavailable / 1024 / 1024 / 1024
  memactive = memactive / 1024 / 1024 / 1024

# Show memory output
memactive = round(memactive, 2)
memactive = str(memactive)
memavailable = round(memavailable, 2)
memavailable = str(memavailable)
memtotal = round(memtotal, 2)
memtotal = str(memtotal)
print('')
print(' ============================================')
print(' ' + memactive + ' GiB / ' + memtotal + ' GiB = ' + memavailable + " GiB Available")
print('')
print(' ==========================')
print(" Total running process", numprocess)
print('')
