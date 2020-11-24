#Luis Cisneros
#process_webdata.py
#Processes parced data taken from scraper_script.sh. Compares if the lastest sample taken from the website is
#different than the prevous entry stored in data_log.txt. Sends an email to alert the user if a differnece is found
#First Finished November 11, 2020

import subprocess #used to run comands from inside a python program


DIR = "insert your process_webdata.py file location here" #store the working directory for later use
dateData = subprocess.run(["date"], stdout=subprocess.PIPE, text=True)
date = dateData.stdout #store the date for later use

# run the shell script, scraper.sh, and store the output as text (as opposed to bits) in scriptData.stdout
scriptData = subprocess.run(["sh", DIR + "/scraper_script.sh"], stdout=subprocess.PIPE, text=True)
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
with open(DIR + "/data_log.txt", "a+") as f: #make sure data_log.txt has been created and is in the same file as the program
    f.seek(0) #go to the start of the file
    first_char = f.read(1)
    if not first_char: #if the file is empty then initialize the file
        f.write("Seat: Capacity, Actual, Remaining. Waitlist: Capacity, Actual, Remaining. Date\n")
    else:
        for line in f: #get the last line in the data_log.txt file
            pass
        last_line = line

    f.write("\t%d\t%d\t%d\t\t\t%d\t%d\t%d\t%s" % (seatCap, seatAct, seatRemain, waitCap, waitAct, waitRemain, date))
f.close()

if first_char: #if the file was not previously empty
    lastDataString = last_line.split("\t")
    lastSeatCap = int(lastDataString[1])
    lastSeatAct = int(lastDataString[2])
    lastSeatRemain = int(lastDataString[3])

    lastWaitCap = int(lastDataString[6])
    lastWaitAct = int(lastDataString[7])
    lastWaitRemain = int(lastDataString[8])

    lastData = [lastSeatCap, lastSeatAct, lastSeatRemain, lastWaitCap, lastWaitAct, lastWaitRemain]
    newData = [seatCap, seatAct, seatRemain, waitCap, waitAct, waitRemain]

    if newData!=lastData:

        print("Change in data! Sending out email...")
        #//**********************Send Email***************************//
        import smtplib, string, subprocess

	# Settings
        fromaddr = 'from_email@gmail.com'
        toaddr  = 'to_email@gmail.com'

        # Googlemail login details
        username = 'from_email_username'
        password = 'from_email_password'

        outputMsg = subprocess.run(["cat", DIR + "/data_log.txt"], stdout=subprocess.PIPE, text=True)

        BODY = str.join("\r\n",(
            "From: %s" % fromaddr,
            "To: %s" % toaddr,
            "Subject: VALUES FROM YOUR SCRAPED WEBSITE JUST CHANGED",
            "",
            outputMsg.stdout,
            ) )

        # send the email
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddr, BODY)
        server.quit()
    else:
        print("No change in data. Date checked: %s" % date)
