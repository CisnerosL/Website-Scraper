import subprocess #used to run comands from inside a python program


# run the shell script, scraper.sh, and store the output as text (as opposed to bits) in scriptData.stdout
scriptData = subprocess.run(["sh", "./scraper_script.sh"], stdout=subprocess.PIPE, text=True)
dateData = subprocess.run(["date"], stdout=subprocess.PIPE, text=True)
date = dateData.stdout

#parse the output text from the shell script by spaces into an array
dataString = scriptData.stdout.split()

#convert the text to integers and store the values
seatCap = int(dataString[1])
seatAct = int(dataString[2])
seatRemain = int(dataString[3])

waitCap = int(dataString[6])
waitAct = int(dataString[7])
waitRemain = int(dataString[8])

#do all the file io processes
with open("data_log.txt", "a+") as f: #make sure data_log.txt has been created and is in the same file as the program
    f.seek(0) #go to the start of the file
    first_char = f.read(1)
    if not first_char: #if the file is empty then initialize the file
        f.write("Seat: Capacity, Actual, Remaining. Waitlist: Capacity, Actual, Remaining. Date\n")
        #f.write("\t%d\t%d\t%d\t\t\t%d\t%d\t%d\t" % (seatCap, seatAct, seatRemain, waitCap, waitAct, waitRemain)) #if the program errors here make sure the process is being run in root crontab
        #f.write(date)
    else:
        for line in f: #get the last line in the data_log.txt file
            pass
        last_line = line
        #f.write("\t%d\t%d\t%d\t\t\t%d\t%d\t%d\t" % (seatCap, seatAct, seatRemain, waitCap, waitAct, waitRemain)
        #f.write(date)
    f.write("\t%d\t%d\t%d\t\t\t%d\t%d\t%d\t%s" % (seatCap, seatAct, seatRemain, waitCap, waitAct, waitRemain, date))
    #f.write(date)
f.close()

if first_char: #if the file was not previously empty
    lastDataString = last_line.split("\t")
    print("the last line is %s" % last_line.split("\t"))
    lastSeatCap = int(lastDataString[1])
    lastSeatAct = int(lastDataString[2])
    lastSeatRemain = int(lastDataString[3])

    lastWaitCap = int(lastDataString[6])
    lastWaitAct = int(lastDataString[7])
    lastWaitRemain = int(lastDataString[8])

    lastData = [lastSeatCap, lastSeatAct, lastSeatRemain, lastWaitCap, lastWaitAct, lastWaitRemain]
    newData = [seatCap, seatAct, seatRemain, waitCap, waitAct, waitRemain]

    if newData!=lastData:
        print("Yas")



#Recieve latest data
#compare with the last entry in log
#Process response if the numbers from the two are different
	#execute email script (or just run it here?) with the alert!
#store latest result to log
#Run every 15 min using crontab

#if seatAct > seatCap: #if for some reason the class is over-enrolling the class
#	if seatRemain 
