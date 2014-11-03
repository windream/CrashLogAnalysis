#encoding=utf8
'''
Created on 2012-10-19

@author: Smallfrogs

dumpkey 生成算法必须和java层一样
'''

import os,sys,re
import binascii
import zipfile

from compiler.pycodegen import TRY_FINALLY

dest_dir   = "D:\\crash\\dest";
source_dir = "D:\\crash\\src";
version = "1000063603"

currentLine = [
               "java.lang.RuntimeException", 
               "java.lang.UnsatisfiedLinkError",
               "java.lang.IllegalArgumentException",
               "java.lang.AssertionError",
               "java.lang.SecurityException",
               "java.lang.UnsupportedOperationException",
               "android.database.sqlite.SQLiteException",
               "java.lang.NoClassDefFoundError",
               "android.content.ActivityNotFoundException",
               "android.app.RemoteServiceException",
               "java.lang.IllegalStateException",
               "java.lang.IncompatibleClassChangeError",
               "android.view.WindowManager$BadTokenException",
               "android.database.CursorWindowAllocationException",
               "android.database.sqlite.SQLiteDiskIOException",
               "android.database.sqlite.SQLiteDatabaseLockedException"
               ];

nextLine = [
            "java.lang.OutOfMemoryError", 
            "java.lang.NullPointerException",
            "java.lang.IllegalArgumentException",
            "java.util.NoSuchElementException",
            "java.util.ConcurrentModificationException",
            "java.lang.IndexOutOfBoundsException",
            "java.lang.ArrayIndexOutOfBoundsException",
            "java.util.NoSuchElementException",
            "java.lang.StackOverflowError",
            "java.lang.ExceptionInInitializerError"
            ];               

def getMethod(line):
    for xx in currentLine:
        if (line.find(xx) <> -1):
            hash = binascii.crc32(xx);
            hash = hash & 0xffffffff;
            return 1, hash;

    for xx in nextLine:
        if (line.find(xx) <> -1):
            hash = binascii.crc32(xx);
            hash = hash & 0xffffffff;
            return 2, hash;
        
    return 0, 0;
    
def getVersion(fullpath):
    
    fin = file(fullpath, "rb");
    lines = fin.readlines();
    fin.close();
    
    for line in lines:
        ret = line.find("me");
        if ret <> -1:
            return line[3:];
    
    return "";

def trim(zstr):
    ystr=zstr.lstrip();
    ystr=ystr.rstrip();
    ystr=ystr.strip();
    return ystr;
  
def moveDumpFile(fullsrcfile, dumpkey):
    sourcefullpath = fullsrcfile;
    dstfulldir = dest_dir + "\\" + str(dumpkey);
    dstfullpath = dest_dir + "\\" + str(dumpkey) + "\\" + os.path.basename(fullsrcfile);
    
    try:
        if (False == os.path.exists(dest_dir)):
            os.mkdir(dest_dir);
                            
        if (False == os.path.exists(dstfulldir)):
            os.mkdir(dstfulldir); 
                        
        if (os.path.exists(dstfullpath) == False):
            os.rename(sourcefullpath, dstfullpath);
        else:
            os.remove(sourcefullpath);
    except Exception,e:
        print e;
        return;
                                    
def getDumpKey(fullpath):
    if (fullpath.find(".zip") == -1):
        return;
        #dumpkey = getDumpKeyFromTxt(fullpath);
        #if (0 != dumpkey):
        #    moveDumpFile(fullpath, dumpkey);
        #    return;
    
    dumpkey = 0;
    
    try:
        zipFile = zipfile.ZipFile(fullpath, "r");
        for filename in zipFile.namelist():
            _find = filename.find(version);
            _filename= filename;
            print _find;
            print _filename;
            if (_filename.find(version) != -1):
                dirname = os.path.dirname(fullpath);
                tmpfile = dirname + os.sep + _filename;
                data = zipFile.read(_filename, None);
                targetfile = open(tmpfile, "wb");
                targetfile.write(data);
                targetfile.close();
                
                dumpkey = getDumpKeyFromTxt2(tmpfile);
                dumpkey = trim(dumpkey);
                    
                print dumpkey;
                if (0 != dumpkey):
                    moveDumpFile(tmpfile, dumpkey);
                else:
                    moveDumpFile(tmpfile, 0);
                        
        zipFile.close();
    except:
        basename = os.path.basename(fullpath);
        print "zip error " + basename;

def getDumpKeyFromTxt2(fullpath):
    try:
        fin = file(fullpath, "rb");
    except:
        print fullpath;
        return;
    
    lines = fin.readlines();
    fin.close();
    
    for line in lines:
        ret = line.find("dumpkey=");
        if ret <> -1:
            dumpkey = line[8:];
            return dumpkey;
        
    return 0;
            
def getDumpKeyFromTxt(fullpath):
    try:
        fin = file(fullpath, "rb");
    except:
        print fullpath;
        return;
    
    lines = fin.readlines();
    fin.close();
    
    matchLine = 0;
    reasonHash = 0;
    
    for line in lines:
        
        if (matchLine == 0):
            ret = line.find("----exception stack trace----");
            if ret <> -1:
                matchLine = 1;
                continue;
            
        if (matchLine == 1):
            method, reasonHash = getMethod(line);
            
            if (method == 1):
                _hashLine = "";
                pos = line.find("(");
                if (-1 <> pos):
                    _hashLine = line[0:pos];
                else:
                    _hashLine = line;
                    
                _hashLine = trim(_hashLine);
                _hashLine = _hashLine[3:];  #Skip "at "
                
                hash = binascii.crc32(_hashLine);
                hash = hash & 0xffffffff;
                
                vIn1 = long(hash);
                vIn2 = long(reasonHash);
                
                result = vIn1 + vIn2;
                if (result < 0):
                    print vIn1, vIn2;
                    
                return result; 
                    
            if (method == 2):                                               
                matchLine = 2;
                continue;
            
        if (matchLine == 2):
            _hashLine = "";
            pos = line.find("(");
            if (-1 <> pos):
                _hashLine = line[0:pos];
            else:
                _hashLine = line;
            
            _hashLine = trim(_hashLine);
            _hashLine = _hashLine[3:];  #Skip "at "

            hash = binascii.crc32(_hashLine);
            hash = hash & 0xffffffff;
            
            vIn1 = long(hash);
            vIn2 = long(reasonHash);
             
            result = vIn1 + vIn2;  
            if (result < 0):
                print vIn1, vIn2;
                              
            return result;                 
            
    return 0;

def walkdir(dirname):
    for parent, dirnames, filenames in os.walk(dirname):
        for filename in filenames:            
            getDumpKey(dirname + os.sep + filename);                
                                             
    print "done";
    
def main():
    walkdir(source_dir);
        
if __name__ == '__main__':
    main();
    pass
