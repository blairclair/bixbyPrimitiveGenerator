import json
import array as arr

intArr = []
strArr = []
boolArr = []

def getFile():
	for i in intArr:
		f = open(i + ".model.bxb", "w+")
		f.write("integer (" + i + ") {\ndescription(__DESCRIPTION__)\n}")
		f.close()
	for s in strArr:
		f = open(s + ".model.bxb", "w+")
		f.write("text (" + s + ") {\ndescription(__DESCRIPTION__)\n}")
		f.close()
	for b in boolArr:
		f = open(s + ".model.bxb", "w+")
		f.write("boolean (" + b + ") {\ndescription(__DESCRIPTION__)\n}")
		f.close()

def listIter(listVal):
	for val in listVal:
		if type(val) == dict:
			gothroughForPrimitives(val)

def gothroughForPrimitives(data):
	for key, val in data.items():
		if type(val) == int and key not in intArr:
			intArr.append(str(key))
		elif type(val) == str and key not in strArr:
			strArr.append(str(key))
		elif type(val) == bool and key not in boolArr:
			boolArr.append(str(key))
		elif type(val) == list:
			listIter(val)
		elif type(val) == dict:
			gothroughForPrimitives(val)


def main():
	with open("ditto.json") as f:
		data = json.load(f)
		gothroughForPrimitives(data)
		getFile()
	

if __name__== "__main__":
	main()

