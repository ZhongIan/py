
import fileinput
import subprocess
import sys
a=sys.argv[0]
b=sys.argv[1]

print("filename:",a)
print("param1:",b)


file = input("請輸入...")
print(file)

with fileinput.input(b) as f_input:
    for line in f_input:
        print(line, end='')
        
subprocess.call("pause",shell=True)