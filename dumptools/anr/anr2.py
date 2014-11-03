#!/usr/bin/env python
# Duan Yi
# 2013.7.17

import os, sys
import anr_ftp, anr_unzip, anr_sort2, anr_report

required = ['anr_ftp.py','anr_unzip.py','anr_sort2.py','anr_report.py']
def check_env():
    for f in required:
        if os.path.exists(f) == False:
            return False
    return True

def main(dirname):
    #download
    y = dirname
    #y = "20130717"
    f = anr_ftp.get_ftp()
    r = '/data/app/dump.m.liebao.cn/data_anr/' + y
    l = 'anr_' + y
    anr_ftp.download(f, r, l, "log.txt")

    #unzip
    l_unzip = l + "_unzip"
    anr_unzip.anr_unzip(l, l_unzip)

    #sort
    anr_sort2.anr_sort2(l_unzip)

    #report
    anr_report.anr_report(l_unzip)

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
