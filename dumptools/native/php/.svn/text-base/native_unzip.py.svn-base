#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.11
import os
import sys


def unzip_dir(src, dst):
	if not os.path.exists(dst):
		os.mkdir(dst)
	for root, dirs, files in os.walk(src):
		for f in files:
			if f.endswith(".zip"):
				fn = os.path.join(root, f)
				cmd = "unzip -n " + fn + " -d " + dst
				print cmd
				os.system(cmd)

if __name__ == "__main__":
	unzip_dir(sys.argv[1], sys.argv[2])
