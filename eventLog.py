def readEventLog(year, month, date):
	fo = open("events.txt", "r+")
	val = fo.readlines()

	for s in range(0,len(val)):
		contents = val[s].split("\t")
		events = []
		
		if(contents[0] ==year):
			if(contents[1] == month):
				if(contents[2] == date):
					events.append(contents[3])
	if(len(events) > 0):				
	
		return events
	else:
		return "Nothing planned"

	fo.close()

def writeEventLog( event):
	fo = open("events.txt", "a+")
	fo.write("\n" + event)
	print(event)
	fo.close()
		

