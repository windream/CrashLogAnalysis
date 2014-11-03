#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.8

import os, sys
import anr_ftp, anr_unzip, anr_sort, anr_report

required = ['anr_ftp.py', 'anr_unzip.py', 'anr_sort.py', 'anr_report.py']
def check_env():
	for f in required:
		if os.path.exists(f) == False:
			return False
	return True

def main():
	#download from ftp
	y = anr_ftp.get_yesterday()
	f = anr_ftp.get_ftp()
	r = '/data_anr/'+ y
	l = 'anr_'+ y
	anr_ftp.download(f, r, l, "log.txt")
	#unzip
	l_unzip = l + "_unzip"
	anr_unzip.anr_unzip(l, l_unzip)
	#sort
	anr_sort.anr_sort(l_unzip)
	#report
	anr_report.anr_report(l_unzip)

if __name__ == "__main__":
	if check_env() == False:
		print "please check required files", required
		sys.exit(-1)	
	main()
	sys.exit(0)