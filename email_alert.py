import smtplib, string, subprocess

# INSTALLING pifind
# Add this line to /etc/rc.local
# python /home/pi/pifind.py
# And place this file, pifind.py in your /home/pi folder, then
# sudo chmod 755 /home/pi/pifind.py
DIR = subprocess.run(["pwd"], stdout=subprocess.PIPE, text=True)

# Settings
fromaddr = 'from_email@gmail.com'
toaddr  = 'to_email@gmail.com'

# Googlemail login details
username = 'from_email_username'
password = 'from_email_password'

outputMSG = subprocess.run(["cat", DIR+"/data_log.txt"], stdout=subprocess.PIPE, text=True)

BODY = string.join((
        "From: %s" % fromaddr,
        "To: %s" % toaddr,
        "Subject: VALUES FROM YOUR SCRAPED WEBSITE JUST CHANGED",
        "",
        outputMsg,
        ), "\r\n")

# send the email
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, BODY)
server.quit()
