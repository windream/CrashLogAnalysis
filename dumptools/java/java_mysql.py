#!/usr/bin/env python
# Duan Yi
# 2013.7.25

import MySQLdb,os,re

def get_param(fullpath,version,dumpkey,dn):
	param = ()
	try:
		fin = file(fullpath,"rb")
		lines = fin.readlines()
		fin.close()
	except Exception,e:
		print e
		return None
	
	buildno=channel=appflags=imei=debug=board=bootloader=brand=cpu_abi=cpu_abi2=device=\
	display=fingerprint=hardware=host=id=manufacturer=model=product=radio=tags=type=user=codename=\
	incremental=release=sdk=dalvikPss=nativePss=otherPss=dalvikPrivateDirty=nativePrivateDirty=\
	otherPrivateDirty=dalvikShareDirty=nativeShareDirty=otherShareDirty=dumpkey=logName=logLocation=""
	
	#buildno=channel=appflags=debug=imei=board=bootloader=brand=cpu_abi=cpu_abi2=device=display=fingerprint=hardware=host=id=manufacturer=model=product=radio=tags=type=user=codename=incremental=release=sdk=dalvikPss=nativePss=otherPss=dalvikPrivateDirty=nativePrivateDirty=otherPrivateDirty=dalvikShareDirty=nativeShareDirty=otherShareDirty=dumpkey=logName=logLocation=""
	
	for line in lines:
		rbuildno = line.find("buildno=")
		if rbuildno != -1:
			r = line.find("=")
			buildno = line[r+1:]
			buildno = buildno.strip()
			continue
			
		rchannel = line.find("channel=")
		if rchannel != -1:
			r = line.find("=")
			channel = line[r+1:]
			channel = channel.strip()
			continue
			
		rappflags = line.find("appflags=")
		if rappflags != -1:
			r = line.find("=")
			appflags = line[r+1:]
			appflags = appflags.strip()
			continue
			
		rdebug = line.find("debug=")
		if rdebug != -1:	
			r = line.find("=")
			debug = line[r+1:]
			debug = debug.strip()
			#if debug == "true":
			#	debug = True
			#else:
			#	debug = False
			continue
			
		rimei = line.find("imei=")
		if rimei != -1:
			r = line.find("=")
			imei = line[r+1:]
			imei = imei.strip()
			continue
			
		rboard = line.find("board=")
		if rboard != -1:
			r = line.find("=")
			board = line[r+1:]
			board = board.strip()
			continue
			
		rbootloader = line.find("bootloader=")
		if rbootloader != -1:
			r = line.find("=")
			bootloader = line[r+1:]
			bootloader = bootloader.strip()
			continue
			
		rbrand = line.find("brand=")
		if rbrand != -1:
			r = line.find("=")
			brand = line[r+1:]
			brand = brand.strip()
			continue
			
		rcpu_abi = line.find("cpu_abi=")
		if rcpu_abi != -1:
			r = line.find("=")
			cpu_abi = line[r+1:]
			cpu_abi = cpu_abi.strip()
			continue
			
		rcpu_abi2 = line.find("cpu_abi2=")
		if rcpu_abi2 != -1:
			r = line.find("=")
			cpu_abi2 = line[r+1:]
			cpu_abi2 = cpu_abi2.strip()
			continue
			
		rdevice = line.find("device=")
		if rdevice != -1:
			r = line.find("=")
			device = line[r+1:]
			device = device.strip()
			continue
			
		rdisplay = line.find("display=")
		if rdisplay != -1:
			r = line.find("=")
			display = line[r+1:]
			display = display.strip()
			continue
			
		rfingerprint = line.find("fingerprint=")
		if rfingerprint != -1:
			r = line.find("=")
			fingerprint = line[r+1:]
			fingerprint = fingerprint.strip()
			continue
			
		rhardware = line.find("hardware=")
		if rhardware != -1:
			r = line.find("=")
			hardware = line[r+1:]
			hardware = hardware.strip()
			continue
			
		rhost = line.find("host=")
		if rhost != -1:
			r = line.find("=")
			host = line[r+1:]
			host = host.strip()
			continue
			
		rid = line.find("id=")
		if rid != -1:
			r = line.find("=")
			id = line[r+1:]
			id = id.strip()
			continue
			
		rmanufacturer = line.find("manufacturer=")
		if rmanufacturer != -1:
			r = line.find("=")
			manufacturer = line[r+1:]
			manufacturer = manufacturer.strip()
			continue
			
		rmodel = line.find("model=")
		if rmodel != -1:
			r = line.find("=")
			model = line[r+1:]
			model = model.strip()
			continue
			
		rproduct = line.find("product=")
		if rproduct != -1:
			r = line.find("=")
			product = line[r+1:]
			product = product.strip()
			continue
			
		rradio = line.find("radio=")
		if rradio != -1:
			r = line.find("=")
			radio = line[r+1:]
			radio = radio.strip()
			continue
		rtags = line.find("tags=")
		if rtags != -1:
			r = line.find("=")
			tags = line[r+1:]
			tags = tags.strip()
			continue
			
		rtype = line.find("type=")
		if rtype != -1:
			r = line.find("=")
			type = line[r+1:]
			type = type.strip()
			continue
			
		ruser = line.find("user=")
		if ruser != -1:
			r = line.find("=")
			user = line[r+1:]
			user = user.strip()
			continue
			
		rcodename = line.find("codename=")
		if rcodename != -1:
			r = line.find("=")
			codename = line[r+1:]
			codename = codename.strip()
			continue
			
		rincremental = line.find("incremental=")
		if rincremental != -1:
			r = line.find("=")
			incremental = line[r+1:]
			incremental = incremental.strip()
			continue
			
		rrelease = line.find("release=")
		if rrelease != -1:
			r = line.find("=")
			release = line[r+1:]
			release = release.strip()
			continue
			
		rsdk = line.find("sdk=")
		if rsdk != -1:
			r = line.find("=")
			sdk = line[r+1:]
			sdk = sdk.strip()
			continue
			
		rdalvikPss = line.find("dalvikPss (KB)")
		if rdalvikPss != -1:
			r = line.find(":")
			dalvikPss = line[r+1:]
			dalvikPss = dalvikPss.strip()
			continue
			
		rnativePss = line.find("nativePss (KB)")
		if rnativePss != -1:
			r = line.find(":")
			nativePss = line[r+1:]
			nativePss = nativePss.strip()
			continue
			
		rotherPss = line.find("otherPss (KB)")
		if rotherPss != -1:
			r = line.find(":")
			otherPss = line[r+1:]
			otherPss = otherPss.strip()
			continue
			
		rdalvikPrivateDirty = line.find("dalvikPrivateDirty (KB)")
		if rdalvikPrivateDirty != -1:
			r = line.find(":")
			dalvikPrivateDirty = line[r+1:]
			dalvikPrivateDirty = dalvikPrivateDirty.strip()
			continue
			
		rnativePrivateDirty = line.find("nativePrivateDirty (KB)")
		if rnativePrivateDirty != -1:
			r = line.find(":")
			nativePrivateDirty = line[r+1:]
			nativePrivateDirty = nativePrivateDirty.strip()
			continue
			
		rotherPrivateDirty = line.find("otherPrivateDirty (KB)")
		if rotherPrivateDirty != -1:
			r = line.find(":")
			otherPrivateDirty = line[r+1:]
			otherPrivateDirty = otherPrivateDirty.strip()
			continue
			
		rdalvikSharedDirty = line.find("dalvikSharedDirty (KB)")
		if rdalvikSharedDirty != -1:
			r = line.find(":")
			dalvikSharedDirty = line[r+1:]
			dalvikSharedDirty = dalvikSharedDirty.strip()
			continue
			
		rnativeSharedDirty = line.find("nativeSharedDirty (KB)")
		if rnativeSharedDirty != -1:
			r = line.find(":")
			nativeSharedDirty = line[r+1:]
			nativeSharedDirty = nativeSharedDirty.strip()
			continue
			
		rotherSharedDirty = line.find("otherSharedDirty (KB)")
		if rotherSharedDirty != -1:
			r = line.find(":")
			otherSharedDirty = line[r+1:]
			otherSharedDirty = otherSharedDirty.strip()
			continue
			
		rdumpkey = line.find("dumpkey=")
		if rdumpkey != -1:
			r = line.find("=")
			dumpkey = line[r+1:]
			dumpkey = dumpkey.strip()
			continue
	
	ln = re.split(r""+os.sep+"",fullpath)
	logName = ln[-1]	
	return (version,buildno,channel,appflags,debug,imei,board,bootloader,brand,cpu_abi,cpu_abi2,device,
display,fingerprint,hardware,host,id,manufacturer,model,product,radio,tags,type,user,codename,incremental,
release,sdk,dalvikPss,nativePss,otherPss,dalvikPrivateDirty,nativePrivateDirty,otherPrivateDirty,dalvikSharedDirty,
nativeSharedDirty,otherSharedDirty,dumpkey,logName,dn)

def java_mysql_insert(src_fn,version,dumpkey,dn):
	try:
		conn = MySQLdb.connect(host = "localhost",user = "root",passwd = "123",db = "DumpLog",charset = "utf8")
		cursor = conn.cursor()
		sql = "insert into Java(me,buildno,channel,appflags,debug,imei,board,bootloader,brand,cpu_abi,cpu_abi2,device,display,fingerprint,hardware,host,id,manufacturer,\
		model,product,radio,tags,type,user,codename,incremental,myrelease,sdk,dalvikPss,nativePss,otherPss,dalvikPrivateDirty,\
		nativePrivateDirty,otherPrivateDirty,dalvikSharedDirty,nativeSharedDirty,otherSharedDirty,dumpkey,logName,logLocation) \
		values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		param = get_param(src_fn,version,dumpkey,dn)
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
	#java_mysql(sys.argv[1])
	sys.exit(0)
