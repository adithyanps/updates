import sys
fout = open('file.txt','w')
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = "the emblem of our land.\n"
fout.write(line2)
x = 52
fout.write(str(x))
fout.close()
print fout
