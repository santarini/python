#!Python 3

import os
import datetime

f = open("GitLog.txt","a")
timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
f.write("Completed: " + timenow + "\n")
f.close() 
