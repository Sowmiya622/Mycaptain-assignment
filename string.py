#implement string function from w3schools
a="Hello sowmiya good day sowmiya"
print(a)
print(a[2])

print(a.capitalize())
print(a.casefold())
b="apple"
print(b.center(25))
print(a.count("sowmiya"))

print(a.encode())
print(a.endswith("."))

t="my\tname\tis\tsam"
print(t.expandtabs(4))

print(a.find("sowmiya"))

x="for only {price:.2f} Rupees!"
print(x.format(price=1000))

print(a.index("d"))
print(a.isalnum())
print(a.isalpha())
print(a.isascii())

print(a.isdigit())
print(a.isidentifier())
print(a.islower())
print(a.isnumeric())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.isupper())
print("#".join(a))

y="apple"
x=y.ljust(10)
print(x,"is my favorite fruit.")

print(a.lower())

v="       mango        "
x=v.lstrip()
print("of all fruit",x,"is my favorite")

x="hello sam"
m=x.maketrans("s","p")
print(x.translate(m))

print(a.partition("apple"))

print(a.replace("o","a"))
print(a.rfind("good"))

x=b.rjust(20)
print(x,"is my favorite fruit")

s="good day sowmiya"
print(s.rpartition("sowmiya"))

print(a.rsplit(","))

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

print(a.split())
print(a.splitlines())
print(a.startswith("Hello"))

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

print(a.swapcase())
print(a.title())
mydict = {83:  80}

txt = "hello sam!"

print(txt.translate(mydict))
print(a.upper())

txt="40"
print(txt.zfill(10))

