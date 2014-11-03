#!/usr/bin/env python
import os,sys
import native_unzip, native_strip, native_bt
import shutil, glob

def main(src):
	#print src 
	if os.path.exists("result"):
		shutil.rmtree("result")
	os.mkdir("result")
	if src.endswith(".zip"):
		os.system("unzip -n " + src + " -d result")
	elif src.find(".dmp") <> -1:
		bn = os.path.basename(src)
		shutil.move(src,os.path.join("result", bn))
	else:
		print "not supported file ext"
		return
	fs = glob.glob("result/*")
	for f in fs:
		print f+"<br>"
		fn = os.path.basename(f)
		head = os.path.join("result", fn + ".head")
		dst = os.path.join("result", fn + ".raw")
		#print dst
		native_strip.native_strip_dump(f, head, dst)
		if not os.path.exists(dst):
			print "strip dump file error"
			return
		bt_file = os.path.join("result", fn + ".log")
		cmd = "../minidump_stackwalk " + dst + " ../symbols 1>" + bt_file + " 2>/dev/null"
		#print cmd+"<br>"
		os.system(cmd)
		if not os.path.exists(bt_file):
			print "get back trace error"
			return
		print "<pre>" + open(bt_file, "r").read() + "</pre>"
	
			
if __name__ == "__main__":
	main(sys.argv[1])
