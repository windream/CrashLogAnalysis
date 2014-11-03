#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.8
# Duan Yi
# 2013.7.23

import os, sys, re, shutil
import native_mysql

so_list = ['libchromeview.so', 'libffmpeg.so', 'libstlport_shared.so', 
			'libvplayer.so', 'libvscanner.so', 'libOMX.14.so', 
			'libvvo.0.so', 'libvao.0.so', 'libvvo.0.so', 'libvvo.9.so', 'libvvo.j.so']

def parse_stack(s):
	#print s
	so = None
	f = None
	ws = s.split()
	#print (ws)
	plus = s.find(" + ")
	exclamation = s.find("!")	
	if exclamation == -1:
		so = ws[1]
	else:		
		so = ws[1].split('!')[0]
		for w in ws:
			if w.startswith("["):
				f = w[1:]
	#print so,f
	return {'so':so, 'file':f}

def search_content(c):	
	result = {}
	start = c	
	ls = c.split('\n')
	for l in ls:
		if l.find(" + ") <> -1:
			result = parse_stack(l)
			if result['so'] in so_list:
				return result
	return None	

def process_log(l):		
	c = open(l, "r").read()
	start = c.find("(crashed)")
	if start == -1:
		return None
	end = c.find("Thread ", start)	
	result = search_content(c[start:end])
	if result == None or 'so' not in result:		
		return result	
	return result

def native_find_name(head, name):
	#print head
	head_line = '-----'
	vindex = head.find(name)
	if vindex == -1:
		return "NoVersion"
	lindex = head.find(head_line, vindex)
	if lindex == -1:
		return head[vindex + len(name):].strip()
	else:
		return head[vindex + len(name):lindex].strip()

log_dir = None
def native_get_version(log_file):
	global log_dir
	hf = ""
	if log_dir == None:
		hf = log_file.replace("_result", "_strip").replace(".log", ".head")
	else:
		hf = os.path.join(log_dir, os.path.basename(log_file)).replace(".log", ".head")	
	#print hf
	if not os.path.exists(hf):
		return None
	hc = open(hf, "r").read()
	v = native_find_name(hc, '"ver"')
	return v

def native_sort(log):
	p_other = os.path.join(log, "others")
	#if not os.path.exists(p_other):
		#os.mkdir(p_other)
	for root, dirs, files in os.walk(log):
		for f in files:			
			if not f.endswith(".log"):
				continue
			fn = os.path.join(root, f)			
			dst_log = log
			v = native_get_version(fn)
			if v != None:
				dst_log = os.path.join(log, v)
				if not os.path.exists(dst_log):
					os.mkdir(dst_log)
				p_other = os.path.join(dst_log, "others")
			r = process_log(fn)
			if r == None:
				#print fn, "not in so list"
				if not os.path.exists(p_other):
					os.mkdir(p_other)
					
				dn = os.path.join(p_other, f)
				if(v != "NoVersion"):
					try:
						native_mysql.native_mysql_insert(fn,v,dn)
					except Exception,e:
						print dn
						print e
				shutil.move(fn, dn)
				pass
			else:
				#print fn, r
				dst = os.path.join(dst_log, r['so'])
				if not os.path.exists(dst):
					os.mkdir(dst)
				if r['file'] != None:
					dst_f = os.path.join(dst, r['file'])
					if not os.path.exists(dst_f):
						os.mkdir(dst_f)
					
					dn = os.path.join(dst_f, f)
					if(v != "NoVersion"):
						try:
							native_mysql.native_mysql_insert(fn,v,dn)
						except Exception,e:
							print dn
							print e
					shutil.move(fn, dn)
				else:
					dn = os.path.join(dst, f)
					if(v != "NoVersion"):
						try:
							native_mysql.native_mysql_insert(fn,v,dn)
						except Exception,e:
							print dn
							print e
					shutil.move(fn, dn)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "cmd log_dir"
		sys.exit(0)
	if len(sys.argv) >= 3:
		log_dir = sys.argv[2]
	native_sort(sys.argv[1])
	#r = process_log(sys.argv[1])
	#if r == None:
	#	print "not in so list"
	#else:
	#	print r['so']
	sys.exit(0)
