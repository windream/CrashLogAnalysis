#!/usr/bin/env python
# Duan Yi
# 2013.7.19

import os, sys, re, shutil
import anr_mysql

so_list = ['libchromeview.so', 'libffmpeg.so', 'libstlport_shared.so', 
			'libvplayer.so', 'libvscanner.so', 'libOMX.14.so', 
			'libvvo.0.so', 'libvao.0.so', 'libvvo.0.so', 'libvvo.9.so', 'libvvo.j.so']

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
			dumpkey = line[3:]
			dumpkey = dumpkey.strip()
			return dumpkey;
        
	return 0

def get_dir(bt):    
	p1 = r"#[0-9][0-9]"
        p2 = r"at com.ijinshan."
	a1 = re.split(p1, bt, re.M)
        a2 = re.split(p2, bt, re.M)
	if (len(a2) < 2 and len(a1) > 1):
		ss = "Native"
		for so in so_list:
			if bt.find(so) <> -1:
				ss += so
				return ss
		#p3 = r"pc [a-f|0-9]*  "
		#a3 = re.split(p3, bt, re.M)
		#if len(a3) > 1:
		#s = a3[1]
		#s = s.replace('/','_')
		#r = r"[ |\n]"
		#s = re.split(r, s)
		#ss += s[0]
		p3 = r"at "
		a3 = re.split(p3, bt, re.M)
		if len(a3) > 1:
			s = a3[1]
			s = s.split(')')
        		ss += "_" + s[0] + ")"
  		return ss
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
	p = r"prio=[0-9]* tid=[0-9]*"
	a = re.split(p, c, re.M)
	if len(a) < 2:
		return None
	return a[1]

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
		
	main_bt = get_stack(content)
	if main_bt == None:
		return
		
	#t = find_type(main_bt)
	t = get_dir(main_bt)
	t = version + os.sep + t
	print t
	d = os.path.join(root, t)
	print d
	if os.path.exists(d) == False:
		os.mkdir(d)
		
	dn = os.path.join(d, fn)
	if(version != "NoVersion"):
		try:
			anr_mysql.anr_mysql_insert(src_fn,version,dn)
		except Exception,e:
			print e
			
	shutil.move(src_fn, dn)


def anr_sort2(src):
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
	anr_sort2(src)
