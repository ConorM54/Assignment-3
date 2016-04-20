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
	print (events)				
	return events

	fo.close()

def writeEventLog(year, month, date, event):
	fo = open("events.txt", "a+")
	val = fo.readlines()
	for s in range(0,len(val)):
		contents = val[s].split("\t")
		
		if(contents[0] ==year):
			if(contents[1] == month):
				if(contents[2] == date):
					fo.write(event)
	fo.close()
		

