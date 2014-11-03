#coding:utf-8
#/usr/bin/python


import zipfile, os, sys

outfolder = None
outfolder2 = None
outfolder3 = None
outfolder4 = None

def parse(folder, dst):
    global outfolder
    global outfolder2
    global outfolder3
    global outfolder4
    
    if not os.path.exists(dst):
        os.mkdir(dst)        
    outfolder = os.path.realpath(os.path.join(dst, "out"))
    outfolder2 = os.path.realpath(os.path.join(dst, "out_raw"))
    outfolder3 = os.path.realpath(os.path.join(dst, "out_dump"))
    outfolder4 = os.path.realpath(os.path.join(dst, "out_err"))
    
    out_folders = [outfolder, outfolder2, outfolder3, outfolder4]
    for _folder in out_folders:
        try:
            if not os.path.exists(_folder):
                os.mkdir(_folder)
        except:
            pass
        
        
    for root, folders, files in os.walk(folder):
        for f in files:
            fpath = os.path.join(root, f)
            if zipfile.is_zipfile(fpath) and f != "symbols.zip":
                unzip(fpath)
            else:
                print "ignore file: ", fpath
            
            
def unzip(fname):
    global outfolder
    global outfolder2
    
    print "unzip: ", fname
    zip = zipfile.ZipFile(fname, "r", zipfile.ZIP_DEFLATED)
    for item in zip.filelist:
        targetname = os.path.join(outfolder, item.filename)
        try:
            _tmp_ = os.path.split(targetname)[0]
            if not os.path.exists(_tmp_):
                os.makedirs(_tmp_)
        except Exception, e:
            print " ****", e
            
        data = zip.read(item.filename)
        pos = data.find("MDMP")
        if (pos < 0): continue
        
        print "out: ", item.filename
        
        target = os.path.join(outfolder, item.filename) 
        open(target, "wb").write(data[pos:])
        open(os.path.join(outfolder2, item.filename), "wb").write(data)
        dump(targetname)
        

def dump(fpath):
    global outfolder3
    global outfolder4
    
    parent, fname = os.path.split(fpath)
    
    #./minidump_stackwalk ./sample.dmp ./symbols 1>sample_std.log 2>sample_err.log
    out_file = os.path.join(outfolder3, fname + ".log")
    #err_file = os.path.join(outfolder4, fname + ".log")
    err_file = '/dev/null'
    cmd = "./minidump_stackwalk " + fpath + " ./symbols 1>" + out_file + " 2>" + err_file
    
    print cmd
    os.system(cmd)
    
    print "dump"


if __name__ == "__main__":
    parse('20130705','20130705')
    
    print "finish"    
