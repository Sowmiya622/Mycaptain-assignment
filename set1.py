#set

n={"apple","banana","cherry"}
color={"green","yellow","apple"}
print(color)
print(n)
print(len(n))
print(n.isdisjoint(color))
print(n.issubset(color))
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y) 

print(z)
z = n.intersection(color) 

print(z)
z = n.intersection_update(color) 
print(z)


print(n.union(color))
print(n.difference(color))
n.difference_update(color)
print(n)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
x.symmetric_difference_update(y)

print(x)

print(type(n))
print("banana" in n)
n.add("orange")
print(n)

n.update(color)
print(n)
print(n.pop())
n.discard("banana")
print(n)
x.remove("banana")
print(n)
print(n.clear())
print(n.copy())

