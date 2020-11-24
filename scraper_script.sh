#Future TODO: Put URL(s) in a separate txt file that the script reads from and output to a separate file for every URL
MY_URL="https://banner.mines.edu/prod/owa/bwckschd.p_disp_detail_sched?term_in=202110&crn_in=10629" #Insert website name here
curl $MY_URL | html2text | #Retrieve only the text from all the HTML code

sed -n '/Seats/,$p'| #Begining of parsed text (this line is included)
sed -n '/Prerequisites:/q;p' #End of parsed text (this line is cut out)

BASEDIR=$PWD
OUTFILENAME="/data_log.txt" #Make sure this file is created and at the same file level as this script
OUTFILEDIR=$BASEDIR$OUTFILENAME #Get the output file path

#-------------notes to self--------------------
#Use chmod +x filename.sh to make a shell file executable
#https://data36.com/web-scraping-tutorial-episode-1-scraping-a-webpage-with-bash/   <----- Website with instructions
