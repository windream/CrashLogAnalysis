#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.8

import os, sys, zipfile

def anr_unzip_cmd(src, dst):
	zfile = zipfile.ZipFile(src,'r')
	print src
	for filename in zfile.namelist():
		data = zfile.read(filename)
		dst_fn = dst + "__" +filename 
		print "src:" + src + " dst:" + dst_fn
		file = open(dst_fn, 'w+b')
		file.write(data)
		file.close()

def anr_unzip(anr_dir, dst_dir):
	'''unzip all the anr zip files into dst dir'''
	if os.path.exists(anr_dir) == False:
		print "anr director " + anr_dir + " not exist"
		return
	if os.path.exists(dst_dir) == False:
		os.mkdir(dst_dir)
	for root, dirs, files in os.walk(anr_dir):
		for f in files:
			if f.endswith(".zip"):
				fn = os.path.join(root, f)
				dst_fn = os.path.join(dst_dir, f[:f.rfind(".zip")])
				try:
					anr_unzip_cmd(fn, dst_fn)
				except:
					print "unzip error: " + f

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "cmd src_directory dst_dirctory"
		sys.exit(0)
	src = sys.argv[1]
	dst = sys.argv[2]
	if os.path.exists(dst) == False:
		os.mkdir(dst)
	#my_unzip(src, dst)
	anr_unzip(src, dst)
