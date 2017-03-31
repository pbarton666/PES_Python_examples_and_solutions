#py_files_1.py

f=open('afile', 'w')
f.write("hello afile!")

#We'll interrogate the file handler object for some properties
print("What's up with {}?\n".format(f.name))
print("readable?", f.readable())
print("writable?", f.writable())
print("encoding:", f.encoding)

#Check if it's closed
print("\nclosed?", f.closed)
print("Closing now!")
f.close()
print("closed?", f.closed)