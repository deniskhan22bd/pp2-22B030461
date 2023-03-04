import os
import shutil

path = os.getcwd() + "/tsis_3"

#1.1
"""
dirslist = []
fileslist = []
for root, dirs, files in os.walk(path):
    for name in dirs:
        dirslist.append(name)
    for name in files:
        fileslist.append(name)

print(dirslist)
print(fileslist)
"""

#1.2
"""
for root, dir, file in os.walk(path):
    print(dir)
    print(file)
    break
"""

#2
"""
print(os.access(path, mode= os.F_OK))
print(os.access(path, mode= os.R_OK))
print(os.access(path, mode= os.W_OK))
print(os.access(path, mode= os.X_OK))
"""

#3
"""
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("file not found")
"""

#4
"""
f = open("tsis_6/row.txt", encoding= "utf-8")
data = f.readlines()
print(len(data))
f.close()
"""

#5
"""
somelist = ["513513531", 123, "gdfigni", True, "provet"]
f = open("tsis_6/filefor5ex.txt", mode="w")
for i in somelist:
    f.write(str(i) + "\n")
f.close()
"""

#6
"""
upperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in upperletters:
    f = open(f"tsis_6/files/{i}.txt", "w")
    f.close()
"""

#7
"""
sourcepath = "tsis_6/row.txt"
destinationpath = "tsis_6/filefor7ex.txt"
shutil.copy(sourcepath, destinationpath)
"""

#8
"""
path = "tsis_6/files/A.txt"
if os.path.exists(path):
    os.remove(path)
    print("deleted")
else:
    print("file doesn't exist")
"""