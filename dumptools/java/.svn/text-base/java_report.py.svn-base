#!/usr/bin/env python
# Duan Yi
# 2013.7.22

import glob, os, sys

def html_report(data, sum, cap):
	html = "<table border='1' cellspacing='0px'>\n"	
	html += '<caption> Version:' + cap + ' </caption>\n'
	html += '<tr><th>'+'Class'+'</th><th>'+"Number"+'</th><th>' + "Percentage" +'</th></tr>\n'
	for d in sorted(data, key=data.get, reverse = True):		
		per = "%.2f"%((data[d] * 100.0)/sum)
		print d, data[d], per
		f = d.split(os.sep)
		html += '<tr><td><a href="'+ f[1] + os.sep + f[2] + '">' + f[2] +'</a></td><td>'+str(data[d])+'</td><td>' + per +'</td></tr>\n'
	html += '<tr><td>'+'Sum'+'</td><td>'+str(sum)+'</td><td>' + "100" +'</td></tr>\n'
	html += '</table>\n'
	return html


def java_report(src):
	data = {}
	sum = 0
	c = ""
	for root, versions, ds in os.walk(src):
		if root != src:
			continue
		for version in sorted(versions, key = str.lower, reverse = True):
			sum = 0
			data = {}
			dd = os.path.join(root, version)
			for d_version, dirs, files in os.walk(dd):
				for d in dirs:
					p = os.path.join(d_version, d) + os.sep + "*"
					s = len(glob.glob(p))
					sum += s
					d = d_version + os.sep + d
					data[d] = s
			c += "<br/><br/>" + html_report(data, sum, version)
	open(os.path.join(src, "index.html"), "w").write(c)
	open("all.html", "a").write(c)


if __name__ == "__main__":	
	if len(sys.argv) < 2:
		print "cmd trace_dir"
		sys.exit(0)
	src = sys.argv[1]	
	java_report(src)
