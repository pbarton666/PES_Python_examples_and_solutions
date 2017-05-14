#!/usr/local/bin/python3

#py_format.py

#number the fields - it's all or nothing
fmt = "{2}, {1}, {0}.".format("George", "Paul", "John")
print(fmt)
print()

#name the fields for readability - use (key, value) pairs
fmt="{who} is a smart {what}".format(what='cookie', who='Sylvia')
print(fmt)
print()

#It's possible to use subscripts in the format string
fmt = "The 5th element of the 1st argument is {0[5]}".\
	     format(["Dallas", "Zorg", "Cornelius", "Ruby", "Billy", "Leelo"])
print(fmt)
print()

#You can also do lookups.  Here are a couple flavors
d = {'Cher':"Sarkisian", "Sonny":"Bono"}
fmt = "Sonny's first name is : {0[Sonny]]"
print(fmt)
print()

#Specify field width, alignment
fmt="Cher's surname is {lookup[Cher]}"
print(fmt.format(lookup=d))
print()

#You can loop through a dictionary and format the contents
for first, last in d.items():
	print("{0:10} {0:10}".format(first, last))
print()
	
#Here's how to specify number formats
fmt="{0:>6} = {0:>#16b} = {0:#06x}"
for i in 1, 23, 456, 7890:
	print(fmt.format(i))
print()
	
#Alternatively you can specifically variable types:

data = [ ("Steve",   59, 202),
         ("Dorothy", 49, 156),
         ("Simon",   39, 155),
         ("David",   61, 135)
        ]
fmt="{0:<12s} {1:4d}  {2:4d}."
for name, age, weight in data:
	print(fmt.format(name, age, weight))
