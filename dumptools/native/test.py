#!/usr/bin/env python
# Duan Yi
# 2013.7.26

import os,sys

def get_param():
	param = ()
	try:
		fin = file("aaa","rb")
		lines = fin.readlines()
		fin.close()
		print lines
		#for line in lines:
		#	print line
		#for i in range(len(lines)):
		#	print lines[i]
		for i in range(len(lines)):
			if lines[i].find("a") != -1:
				print lines[i]
				i += 2
				print lines[i]
	except Exception,e:
		print e
		return None
		
if __name__ == "__main__":
	
	get_param()
	sys.exit(0)
