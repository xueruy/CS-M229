#free -m to get memory usage
#time package to get cpu runtime

import os
import time

import subprocess

tot_test_files = 0
print '......Please wait......'

os.system("free | awk 'FNR == 2 {print $3}'") #"before" memory use
start = time.clock()

os.system("OMP_NUM_THREADS=1 python basecall.py /home/ubuntu/dataplace/MAP006-1/MAP006-1_downloads/pass/LomanLabz_PC_Ecoli_K12_MG1655_20150924_MAP006_1_5005_1_ch509_file80_strand.fast5")
end = time.clock()
os.system("free | awk 'FNR == 2 {print $3}'") #"after" memory use

print 'Program run-time in your CPU: ' + str(int(end - start)) + ' seconds, for', tot_test_files, 'files'