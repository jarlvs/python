phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

for name, number in phonebook.items():
	print name
	print number
will 'print' out  first key and then there number for all 
keys.

for name in phonebook.items():
	print name
'print' all key vaue pair.

del phonebook["John"] wil delect key-value pair of John.
