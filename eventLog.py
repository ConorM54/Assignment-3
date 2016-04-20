def readEventLog():
	with open("events.txt", "r") as ins:
	    array = []
	    for line in ins:
	        array.append(line)

    print (array[2]) 
	fo.close()

readEventLog()