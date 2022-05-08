#implement list function from w3school

my_list=["c","c++","python","html"]
my_sub=["lan","eng","maths"]
b=["sow","ram"]
print("'adding two list'",my_list+b)
print("the list is",my_list)
print(len(my_list))
print(my_list[-2])

my_list.append("php")
print(my_list.copy())

print(my_list.count("rmt"))
print(my_list.extend(my_sub))
print(my_list)

my_list.insert(2,"java")
print(my_list.index("c++"))

print(my_list)

my_list.pop(2)
print("list pop",my_list)

my_list.remove("c")
print(my_list)

my_list.sort()
print("sort",my_list)

my_list.sort(reverse=True)
print("reverse list:",my_list)
print(my_list.clear())
