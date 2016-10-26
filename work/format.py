#!/usr/bin/python
#coding=utf-8

def tohex(val):
 return (((val>>3) + (1 << 8)) % (1 << 8))

f1 = open("move_1.txt", "w")
f2 = open("move_1")
i = 0
try:
	for line in f2:
		str = line.split()
		print(len(str))
		for i in range(0,len(str),6):
			#f1.write("%x" %(tohex(int(str[i]))))
			f1.write("%02x%02x%02x" %(tohex(int(str[i])),tohex(int(str[i+1])),tohex(int(str[i+2]))))
			f1.write("%02x" %(0))
			f1.write("%02x%02x%02x" %(tohex(int(str[i+3])),tohex(int(str[i+4])),tohex(int(str[i+5]))))
			f1.write("%02x" %(0))
		#f1.write(str(i))
		#f1.write("%s" %(str2))
		#f1.write(line.strip('\n') + ";\n")
			f1.write("\n")
		#print(line)
			#i += 6
finally:
	f2.close()
	f1.close()