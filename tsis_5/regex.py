import re

f = open ("tsis_5/row.txt", encoding= "utf-8")
data = str(f.readlines())
#1
"""
s = "gfgfabbasf bdfabanb "
r = re.findall(r"ab*", s)
r1 = re.findall(r"ab*", data)
print(r, r1)
"""

#2
"""
r = re.findall(r"ab{2,3}", data)
print(r)
s = "rtewtwabbbtrwtwetds edsgsdgabbsdgst abbbb"
r = re.findall(r"ab{2,3}", s)
print(r)
"""

#3
"""
s = "asbvcbfd_fbdfb_rturtds"
r = re.findall(r"([a-z]+(_[a-z]+)+)", s)
print(r)
r = re.search(r"[a-z]+(_[a-z]+)+", s)
print(r.group())
"""

#4
"""
r = re.findall(r"[A-Z][a-z]+", data)
print(r)

"""

#5
"""
r = re.findall(r"^a.*b$", data)
print(r)
s = "aafdfdfb acb gdf"
r = re.findall(r"^a.*b$", s)
print(r)

"""
#6
"""
r = re.sub(r"[ ,.]", ":", data)
print(r)

"""

#7
"""
s = "_1sdf1_sdgsdff_GSsdf"
while True:
    if re.search(r"(.*?)_([\w])", s):
        x = re.search(r"(.*?)_(\w)", s)
        a = x.group()
        b = x.group(1) + x.group(2).upper()
        r = re.sub(a, b, s)
        s = r
    else:
        break
print(s)
""" 

#8
"""
s = "AbdfbCdsfdsgAfdsgsSbddfbfdb"
r = re.findall(r"[A-Z][^A-Z]*", s)
print(r)  
"""

#9
"""
def insert_space(match):
    return match.group(1) + " " + match.group(2)

s = "aBSdsbsbdbSBSBsbsdbsdbsSBSBSDBSBSD"
r = re.sub(r"(.*?)([A-Z])", insert_space, s)
print(r)
"""

#10
"""
s = "Case1BaseMathCheese"
while True:
    if re.search(r"(.+?)([A-Z])", s):
        r = re.search(r"(.+?)([A-Z])", s)
        a = r.group(1).lower() + "_" + r.group(2).lower()
        x = re.sub(r.group(), a, s)
        s = x
    else:
        break
print(s)
"""