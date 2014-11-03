#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.11

import os, sys, threading

TH_NUM = 8
def native_bt_dump(dump, dst):
	cmd = "./minidump_stackwalk " + dump + " ./symbols 1>" + dst + " 2>/dev/null"
	print cmd
	os.system(cmd)

def threading_main(ss, ds):
	for i in range(len(ss)):
		s = ss[i]
		d = ds[i]
		native_bt_dump(s,d)

def threading_bt(srcs, dsts):
	global TH_NUM
	t = len(srcs)
	sep = t/(TH_NUM-1)
	last = 0
	ts = []
	for i in range(sep, t, sep):
		#print last, i
		th = threading.Thread(target = threading_main, args = (srcs[last:i], dsts[last:i]))
		ts.append(th)
		th.start()
		last = i
	#print last, t
	ts1 = srcs[last:t]
	ts2 = dsts[last:t]
	th = threading.Thread(target = threading_main, args = (ts1, ts2))
	ts.append(th)
	th.start()
	for th in ts:
		th.join()
	print "=====done===="


def native_bt_dir(ddir, dst):
	global TH_NUM
	if not os.path.exists(dst):
		os.mkdir(dst)			
	srcs = []
	dsts = []
	for root, dirs, files in os.walk(ddir):
		for f in files:
			if not f.endswith(".raw"):
				continue
			fn = os.path.join(root, f)
			dfn = os.path.join(dst, f.replace(".raw", ".log"))
			srcs.append(fn)
			dsts.append(dfn)
	threading_bt(srcs, dsts)

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "cmd src dst"
		sys.exit(0)
	native_bt_dir(sys.argv[1], sys.argv[2])
