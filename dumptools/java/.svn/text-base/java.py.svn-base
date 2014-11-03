#!/usr/bin/env python
# Duan Yi
# 2013.7.22

import os, sys
import java_ftp, java_unzip, java_sort, java_report

required = ['java_ftp.py', 'java_unzip.py', 'java_sort.py', 'java_report.py']
def check_env():
	for f in required:
		if os.path.exists(f) == False:
			return False
	return True

def main():
	#download from ftp
	y = java_ftp.get_yesterday()
	f = java_ftp.get_ftp()
	r = '/data_anr/'+ y
	l = 'anr_'+ y
	java_ftp.download(f, r, l, "log.txt")
	#unzip
	l_unzip = l + "_unzip"
	java_unzip.java_unzip(l, l_unzip)
	#sort
	java_sort.java_sort(l_unzip)
	#report
	java_report.java_report(l_unzip)

if __name__ == "__main__":
	if check_env() == False:
		print "please check requred files", requred
		sys.exit(-1)	
	main()
	sys.exit(0)
