
import fileinput
import subprocess

# ===== sys ======
# python "...\filein.py" FileinputTest.txt
import sys
a=sys.argv[0]
b=sys.argv[1]

print("filename:",a)
print("param1:",b)

with fileinput.input(b) as f_input:
    for line in f_input:
        print(line, end='')

# ===== input =====
#file = input("請輸入...")
#print(file)
#
#with fileinput.input(file) as f_input:
#    for line in f_input:
#        print(line, end='')
        
# 暫停        
subprocess.call("pause",shell=True)