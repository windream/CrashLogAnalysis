#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.11

import os, sys

def native_find_name(head, name):
	#print head
	head_line = '-----'
	vindex = head.find(name)
	if vindex == -1:
		return None
	lindex = head.find(head_line, vindex)
	if lindex == -1:
		return head[vindex + len(name):].strip()
	else:
		return head[vindex + len(name):lindex].strip()



def native_strip_dump(src, head, dst):
	print src
	#print head
	#print dst
	data = open(src, "r").read()
	pos = data.find("MDMP")
	if pos == -1:
		return
	open(head, "w").write(data[:pos])
	open(dst, "w").write(data[pos:])


def native_strip_dir(src, dst):
	print src, dst
	if not os.path.exists(dst):
		os.mkdir(dst)
	for root, dirs, files in os.walk(src):
		for f in files:
			if f.rfind(".dmp") <> -1:
				fn = os.path.join(root, f)
				head = os.path.join(dst, f + ".head")
				dst_f = os.path.join(dst, f + ".raw")
				native_strip_dump(fn, head, dst_f)
	return

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "cmd dump_directory dest_directory"
		sys.exit(-1)
	native_strip_dir(sys.argv[1], sys.argv[2])
