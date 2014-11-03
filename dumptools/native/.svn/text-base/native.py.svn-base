#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.8

import os, sys
import native_ftp, native_dump, native_sort, native_report

def main():
	#download from ftp
	y = native_ftp.get_yesterday()
	f = native_ftp.get_ftp()
	r = '/data_native/'+ y
	l = 'native_'+ y
	native_ftp.download(f, r, l, "log.txt")
	#dump analysis
	l_dump = l + "_done"
	native_dump.parse(l, l_dump)
	#sort
	dst = os.path.join(l_dump, "out_dump")
	native_sort.native_sort(dst)
	#report
	native_report.native_report(dst)
	

if __name__ == "__main__":
	main()
	sys.exit(0)