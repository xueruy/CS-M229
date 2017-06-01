#free -m to get memory usage
#time package to get cpu runtime

import os
import time
import subprocess

tot_test_files = 0
print '......Please wait......'

p1 = subprocess.Popen("free | awk 'FNR == 2 {print $3}'", stdout=subprocess.PIPE, shell=True)
(output1, err) = p1.communicate()
start = time.clock()
# os.system("free | awk 'FNR == 2 {print $3}'") #past memory use
# os.system("OMP_NUM_THREADS=1 python basecall.py /home/ubuntu/dataplace/MAP006-1/MAP006-1_downloads/pass/LomanLabz_PC_Ecoli_K12_MG1655_20150924_MAP006_1_5005_1_ch509_file80_strand.fast5")
# os.system("python /Users/seansea/npm-global/demo-app/npm-demo-pkg/ee232e/shellTest.py")
p2 = subprocess.Popen("OMP_NUM_THREADS=1 python basecall.py /home/ubuntu/dataplace/R7.3_E_coli/MAP006-1_downloads/pass/LomanLabz_PC_Ecoli_K12_MG1655_20150924_MAP006_1_restart_0917_1_ch89_file15_strand.fast5", stdout=subprocess.PIPE, shell=True) #work!
(output2, err) = p2.communicate()
print output2
end = time.clock()
# os.system("free | awk 'FNR == 2 {print $3}'") #current memory use
p3 = subprocess.Popen("free | awk 'FNR == 2 {print $3}'", stdout=subprocess.PIPE, shell=True)
(output2, err) = p3.communicate()

print 'Memory change is', (int(output2) - int(output1))
print 'Program run-time in your CPU: ' + str(int(end - start)) + ' seconds, for', tot_test_files, 'files'