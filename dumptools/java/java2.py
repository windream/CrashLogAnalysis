#!/usr/bin/env python
# Duan Yi
# 2013.7.22

import os, sys
import java_ftp, java_unzip, java_sort2, java_report

required = ['java_ftp.py','java_unzip.py','java_sort2.py','java_report.py']
def check_env():
    for f in required:
        if os.path.exists(f) == False:
            return False
    return True

def main(dirname):
    #download
    y = dirname
    #y = "20130717"
    f = java_ftp.get_ftp()
    r = '/data/app/dump.m.liebao.cn/data/' + y
    l = 'java_' + y
    java_ftp.download(f, r, l, "log.txt")

    #unzip
    l_unzip = l + "_unzip"
    java_unzip.java_unzip(l, l_unzip)

    #sort
    java_sort2.java_sort2(l_unzip)

    #report
    java_report.java_report(l_unzip)

if __name__ == "__main__":
    if check_env() == False:
        print "please check required files", required
        sys.exit(-1)
    dirname=''
    if len(sys.argv) >=2:
        dirname=sys.argv[1]
    else:
        dirname=anr_ftp.get_yesterday()

    main(dirname)
    sys.exit(0)
