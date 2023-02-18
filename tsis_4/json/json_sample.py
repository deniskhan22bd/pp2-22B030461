import json

f = open("sample.json")

data = json.load(f)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
print(data["imdata"][0]["l1PhysIf"]["attributes"]["dn"]," " * 28 ,data["imdata"][0]["l1PhysIf"]["attributes"]["speed"], " " , data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"])
print(data["imdata"][1]["l1PhysIf"]["attributes"]["dn"]," " * 28 ,data["imdata"][1]["l1PhysIf"]["attributes"]["speed"], " " , data["imdata"][1]["l1PhysIf"]["attributes"]["mtu"])
print(data["imdata"][2]["l1PhysIf"]["attributes"]["dn"]," " * 28 ,data["imdata"][2]["l1PhysIf"]["attributes"]["speed"], " " , data["imdata"][2]["l1PhysIf"]["attributes"]["mtu"])
