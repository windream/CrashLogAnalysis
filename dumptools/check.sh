#!/bin/bash
echo "anr.py"
diff anr/anr.py /var/www/anr/anr.py
echo "anr_ftp.py"
diff anr/anr_ftp.py /var/www/anr/anr_ftp.py
echo "anr_unzip.py"
diff anr/anr_unzip.py /var/www/anr/anr_unzip.py
echo "anr_sort.py"
diff anr/anr_sort.py /var/www/anr/anr_sort.py
echo "anr_report.py"
diff anr/anr_report.py /var/www/anr/anr_report.py

echo "native.py"
diff native/native.py /var/www/native/native.py
echo "native_ftp.py"
diff native/native_ftp.py /var/www/native/native_ftp.py
echo "native_dump.py"
diff native/native_dump.py /var/www/native/native_dump.py
echo "native_report.py"
diff native/native_report.py /var/www/native/native_report.py
echo "native_sort.py"
diff native/native_sort.py /var/www/native/native_sort.py
echo "native_unzip.py"
diff native/native_unzip.py /var/www/native/native_unzip.py
echo "native_strip.py"
diff native/native_strip.py /var/www/native/native_strip.py
echo "native_bt.py"
diff native/native_bt.py /var/www/native/native_bt.py
echo "native1.py"
diff native/native1.py /var/www/native/native1.py

