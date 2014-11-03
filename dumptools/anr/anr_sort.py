#!/usr/bin/env python
# Xing Xuezhi
# 2013.7.8

import os, sys, re, shutil

TYPE_ADDRESSBAR = 0
TYPE_HOMEPAGE = 1
TYPE_NATIVEPOLL = 2
TYPE_CHROME = 3
TYPE_DOWNLOAD = 4
TYPE_GLES = 5
TYPE_TOOLBAR = 6
TYPE_VIDEO = 7
TYPE_ANDROID = 8
TYPE_OTHERS = 9

def get_type_dir(t):
	global TYPE_ADDRESSBAR
	global TYPE_HOMEPAGE
	global TYPE_NATIVEPOLL
	global TYPE_CHROME
	global TYPE_DOWNLOAD
	global TYPE_GLES
	global TYPE_TOOLBAR
	global TYPE_VIDEO
	global TYPE_ANDROID
	global TYPE_OTHERS
	s = ""
	if t == TYPE_ADDRESSBAR:
		s = "AddressBar"
	if t == TYPE_HOMEPAGE:
		s = "Homepage"
	if t == TYPE_NATIVEPOLL:
		s = "NativePoll"
	if t == TYPE_CHROME:
		s = "Chrome"
	if t == TYPE_DOWNLOAD:
		s = "Download"
	if t == TYPE_GLES:
		s = "GLES"
	if t == TYPE_TOOLBAR:
		s = "Toolbar"
	if t == TYPE_VIDEO:
		s = "Video"
	if t == TYPE_ANDROID:
		s = "Android"
	if t == TYPE_OTHERS:
		s = "Others"
	return s


def get_type_keyword(t):
	global TYPE_ADDRESSBAR
	global TYPE_HOMEPAGE
	global TYPE_NATIVEPOLL
	global TYPE_CHROME
	global TYPE_DOWNLOAD
	global TYPE_GLES
	global TYPE_TOOLBAR
	global TYPE_VIDEO
	global TYPE_ANDROID
	global TYPE_OTHERS
	s = ""
	if t == TYPE_ADDRESSBAR:
		s = ["com.ijinshan.browser.view.impl.SmartAddressBarPopup"]
	if t == TYPE_HOMEPAGE:
		s = ["BrowserActivity.onWindowFocusChanged", "BrowserActivity.onCreate", "GridViewAdapter", "QuickAccessHolder", "QuickAccessExpanListAdapter", "AbsExpandableListAdapter"]
	if t == TYPE_NATIVEPOLL:
		s = ["android.os.MessageQueue.nativePollOnce"]
	if t == TYPE_CHROME:
		s = ["org.chromium", "kchromewebview", "ChromeNativePreferences"]
	if t == TYPE_DOWNLOAD:
		s = ["DownloadScreen", "DownloadManager"]
	if t == TYPE_GLES:
		s = ["GLES", "EGLImpl"]
	if t == TYPE_TOOLBAR:
		s = ["ToolBar"]
	if t == TYPE_VIDEO:
		s = ["com.ijinshan.media"]
	if t == TYPE_ANDROID:
		s = None
	if t == TYPE_OTHERS:
		s = None
	return s
	

def find_type(bt):	
	for t in range(TYPE_OTHERS):
		kws = get_type_keyword(t)
		if kws == None:
			continue
		for k in kws:
			if bt.find(k) <> -1:				
				return t
	return TYPE_OTHERS

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
	main_bt = get_stack(content)
	if main_bt == None:
		return
	t = find_type(main_bt)
	d = os.path.join(root, get_type_dir(t))
	print d
	if os.path.exists(d) == False:
		os.mkdir(d)
	shutil.move(src_fn, os.path.join(d, fn))


def anr_sort(src):
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
	anr_sort(src)
