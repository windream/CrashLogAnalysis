#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.8
# Duan Yi
# 2013.7.23

import os, sys, shutil
import native_ftp, native_unzip, native_strip, native_bt, native_sort, native_report, native_report2, native_merge

def main(dirname):
	#download from ftp
	#y = "20130724"
	y = dirname
	f = native_ftp.get_ftp()
	r = '/data/app/dump.m.liebao.cn/data_native/'+ y
	l = 'native_'+ y
	native_ftp.download(f, r, l, "log.txt")
	#unzip
	l_unzip = l + "_unzip"
	native_unzip.unzip_dir(l, l_unzip)
	#strip
	l_strip = l + "_strip"
	native_strip.native_strip_dir(l_unzip, l_strip)
	#bt
	l_bt = l + "_result"
	l_tmp = l + "_tmp"
	native_bt.native_bt_dir(l_strip, l_tmp)
	#merge
	native_merge.native_merge(l_tmp, l_bt)
	#sort	
	native_sort.native_sort(l_bt)
	#report
	native_report2.native_report2(l_bt)
	#cleanup
	#shutil.rmtree(l)
	#shutil.rmtree(l_unzip)
	#shutil.rmtree(l_strip)

if __name__ == "__main__":
    dirname=''
    if len(sys.argv) >=2:
        dirname=sys.argv[1]
    else:
        dirname=anr_ftp.get_yesterday()

    main(dirname)
    sys.exit(0)
