#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.9

import glob, os, sys

def html_report(data, sum):
	html = "<table border='1' cellspacing='0px'>\n"	
	html += '<tr><th>'+'Class'+'</th><th>'+"Number"+'</th><th>' + "Percentage" +'</th></tr>\n'
	for d in sorted(data, key=data.get, reverse = True):		
		per = "%.2f"%((data[d] * 100.0)/sum)
		print d, data[d], per
		html += '<tr><td><a href="'+d + '">' + d +'</a></td><td>'+str(data[d])+'</td><td>' + per +'</td></tr>\n'
	html += '<tr><td>'+'Sum'+'</td><td>'+str(sum)+'</td><td>' + "100" +'</td></tr>\n'
	html += '</table>'
	return html


def native_report(src):
	data = {}
	sum = 0
	for root, dirs, files in os.walk(src):		
		for d in dirs:
			p = os.path.join(root, d) + os.sep + "*.log"
			s = len(glob.glob(p))
			sum += s
			name = os.path.join(root, d) 
			if name.startswith(src):
				name = name[len(src):]
			if name.startswith("/"):
				name = name[1:]
			data[name] = s	
	c = html_report(data, sum)
	open(os.path.join(src, "index.html"), "w").write(c)


if __name__ == "__main__":	
	if len(sys.argv) < 2:
		print "cmd trace_dir"
		sys.exit(0)
	src = sys.argv[1]	
	native_report(src)
