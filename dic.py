#implement dictionary data struct

mydict={"c":"easy",
        "java":"tough","php":"web"}
print(mydict)
print(mydict.copy())

x=('one','two','three')
y=0
print(dict.fromkeys(x,y))
print(mydict.values())

print(mydict.get("java"))

print(mydict.items())

print(mydict.keys())



print(mydict.update({"color":"white"}))

print(mydict.pop("java"))
print(mydict)

print(mydict.popitem())
print(mydict)
print(mydict.setdefault("c","diffcult"))
print(mydict)
