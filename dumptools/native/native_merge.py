#!/usr/bin/env python
# Duan Yi
# 2013.7.22

import os,sys

def native_merge(tmp,result):
	if not os.path.exists(result):
		os.mkdir(result)
	for root, dirs, files in os.walk(tmp):
		for f in files:
			if not f.endswith(".log"):
				continue
			fn = os.path.join(root, f)
			hn = fn.replace("_tmp", "_strip").replace(".log", ".head")
			dn = fn.replace("_tmp", "_result")
			if not os.path.exists(hn):
				return None
			cmd = "cat " + hn + " " + fn + " >" + dn
			os.system(cmd)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "cmd log_dir"
		sys.exit(0)
	if len(sys.argv) >= 3:
		log_dir = sys.argv[2]
	native_merge(sys.argv[1],sys.argv[2])
	sys.exit(0)
