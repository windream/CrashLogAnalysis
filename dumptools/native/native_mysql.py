#!/usr/bin/env python
# Duan Yi
# 2013.7.26

import MySQLdb,os,re

def get_param(fullpath,version,dn):
	param = ()
	try:
		fin = file(fullpath,"rb")
		lines = fin.readlines()
		fin.close()
	except Exception,e:
		print e
		return None
	
	prod=ver=pid=guid=android_build_id=android_build_fp=device=model=brand=exception_info=\
	ptime=ptype=gpu_venid=gpu_devid=gpu_driver=gpu_psver=gpu_vsver=lsb_release=""
	
		#buildno=channel=appflags=debug=imei=board=bootloader=brand=cpu_abi=cpu_abi2=device=display=fingerprint=hardware=host=id=manufacturer=model=product=radio=tags=type=user=codename=incremental=release=sdk=dalvikPss=nativePss=otherPss=dalvikPrivateDirty=nativePrivateDirty=otherPrivateDirty=dalvikShareDirty=nativeShareDirty=otherShareDirty=dumpkey=logName=logLocation=""
	
	for i in range(len(lines)):
		if lines[i].find("\"prod\"") != -1:
			i += 2
			prod = lines[i]
			prod = prod.strip()
			continue
			
		if lines[i].find("\"ver\"") != -1:
			i += 2
			ver = lines[i]
			ver = ver.strip()
			continue
			
		if lines[i].find("\"pid\"") != -1:
			i += 2
			pid = lines[i]
			pid = pid.strip()
			continue
			
		if lines[i].find("\"guid\"") != -1:
			i += 2
			guid = lines[i]
			guid = guid.strip()
			continue
			
		if lines[i].find("\"android_build_id\"") != -1:
			i += 2
			android_build_id = lines[i]
			android_build_id = android_build_id.strip()
			continue
			
		if lines[i].find("\"android_build_fp\"") != -1:
			i += 2
			android_build_fp = lines[i]
			android_build_fp = android_build_fp.strip()
			continue
			
		if lines[i].find("\"device\"") != -1:
			i += 2
			device = lines[i]
			device = device.strip()
			continue
			
		if lines[i].find("\"model\"") != -1:
			i += 2
			model = lines[i]
			model = model.strip()
			continue
			
		if lines[i].find("\"brand\"") != -1:
			i += 2
			brand = lines[i]
			brand = brand.strip()
			continue
			
		if lines[i].find("\"ptime\"") != -1:
			i += 2
			ptime = lines[i]
			ptime = ptime.strip()
			continue
			
		if lines[i].find("\"ptype\"") != -1:
			i += 2
			ptype = lines[i]
			ptype = ptype.strip()
			continue
			
		if lines[i].find("\"gpu-venid\"") != -1:
			i += 2
			gpu_venid = lines[i]
			gpu_venid = gpu_venid.strip()
			continue
			
		if lines[i].find("\"gpu-devid\"") != -1:
			i += 2
			gpu_devid = lines[i]
			gpu_devid = gpu_devid.strip()
			continue
			
		if lines[i].find("\"gpu-driver\"") != -1:
			i += 2
			gpu_driver = lines[i]
			gpu_driver = gpu_driver.strip()
			continue
			
		if lines[i].find("\"gpu-psver\"") != -1:
			i += 2
			gpu_psver = lines[i]
			gpu_psver = gpu_psver.strip()
			continue
			
		if lines[i].find("\"gpu-vsver\"") != -1:
			i += 2
			gpu_vsver = lines[i]
			gpu_vsver = gpu_vsver.strip()
			continue
			
		if lines[i].find("\"lsb-release\"") != -1:
			i += 2
			lsb_release = lines[i]
			lsb_release = lsb_release.strip()
			continue		
	
	ln = re.split(r""+os.sep+"",fullpath)
	logName = ln[-1]	
	return (prod,ver,pid,guid,android_build_id,android_build_fp,device,model,brand,exception_info,
	ptime,ptype,gpu_venid,gpu_devid,gpu_driver,gpu_psver,gpu_vsver,lsb_release,logName,dn)

def native_mysql_insert(src_fn,version,dn):
	try:
		conn = MySQLdb.connect(host = "localhost",user = "root",passwd = "123",db = "DumpLog",charset = "utf8")
		cursor = conn.cursor()
		sql = "insert into Native(prod,ver,pid,guid,android_build_id,android_build_fp,device,model,brand,exception_info,\
		ptime,ptype,gpu_venid,gpu_devid,gpu_driver,gpu_psver,gpu_vsver,lsb_release,logName,logLocation) \
		values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		param = get_param(src_fn,version,dn)
		if param != None:
			n = cursor.execute(sql,param)
		cursor.close()
		conn.close()
	except Exception,e:
		#print
		print e

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "cmd log_dir"
		sys.exit(0)
	sys.exit(0)
