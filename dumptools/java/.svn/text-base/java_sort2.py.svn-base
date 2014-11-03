#!/usr/bin/env python
# Duan Yi
# 2013.7.22

import os, sys, re, shutil
import java_mysql
import binascii
from compiler.pycodegen import TRY_FINALLY

def get_version(fullpath):
	try:
		fin = file(fullpath, "rb")
	except:
        	print fullpath
        	return 0
    
	lines = fin.readlines()
	fin.close()
    
	for line in lines:
		ret = line.find("me=")
		if ret <> -1:
			version = line[3:]
			version = version.strip()
			return version;
        
	return 0

def get_dumpkey(fullpath):
	try:
		fin = file(fullpath, "rb")
	except:
        	print fullpath
        	return 0
    
	lines = fin.readlines()
	fin.close()
    
	for line in lines:
		ret = line.find("dumpkey=")
		if ret <> -1:
			dumpkey = line[8:]
			dumpkey = dumpkey.strip()
			return dumpkey;
        
	return 0 


def get_dir(bt):    
        p2 = r"at com.ijinshan."
        a2 = re.split(p2, bt, re.M)
	
        if len(a2) < 2:
		ss = "Others"
		p4 = r"at "
		a4 = re.split(p4, bt, re.M)
		if len(a4) > 1:
			s = a4[1]
			s = s.split(')')
        		ss += "_" + s[0] + ")"
		return ss
	s = a2[1]
        s = s.split(')')
        return s[0]+")"

def get_stack(c):
	p1 = r"----exception stack trace----"
	a1 = re.split(p1, c, re.M)
	if len(a1) < 2:
		return None
	p2 = r"-----dumpkey----"
	a2 = re.split(p2, a1[1], re.M)
	if len(a2) < 2:
		return None
	return a2[0]

def my_sort(root, fn):	
	src_fn = os.path.join(root, fn)
	print src_fn
	content = open(src_fn, "r").read()
	
	version = get_version(src_fn)
	if version == 0:
		version = "NoVersion"
	d = os.path.join(root,version)
	if os.path.exists(d) == False:
		os.mkdir(d)
	
	dumpkey = get_dumpkey(src_fn)
	if dumpkey == 0:
		return
		
	main_bt = get_stack(content)
	if main_bt == None:
		return
		
	#t = find_type(main_bt)
	t = get_dir(main_bt)
	t = version + os.sep + dumpkey + "_" + t
	print t
	d = os.path.join(root, t)
	print d
	if os.path.exists(d) == False:
		os.mkdir(d)
	
	dn = os.path.join(d, fn)
	if(version != "NoVersion"):
		#param = java_mysql.get_param(src_fn,version,dumpkey)
		try:
			java_mysql.java_mysql_insert(src_fn,version,dumpkey,dn)
		except Exception,e:
			print e
			
	shutil.move(src_fn, dn)

def java_sort2(src):
	for root, dirs, files in os.walk(src):
		if root != src:
			continue
		for f in files:
			f = f.strip()			
			if f.endswith(".txt"):				
				my_sort(root, f)

if __name__ == "__main__":	
	if len(sys.argv) < 2:
		print "cmd trace_dir"
		sys.exit(0)
	src = sys.argv[1]	
	#my_unzip(src, dst)
	java_sort2(src)
