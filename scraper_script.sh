#date >> /home/lcisnero/Processes/class_crontab_log.txt;

curl "https://banner.mines.edu/prod/owa/bwckschd.p_disp_detail_sched?term_in=202110&crn_in=10629"
#|html2text |
# sed -n '/Total Tests/,$p'|
# sed -n '/303-273-3000/q;p' |
#head -n-5 >> /home/lcisnero/Processes/class_crontab_log.txt;

#echo "$" >> /home/lcisnero/Processes/class_crontab_log.txt

#"tr '\n' ' ' < crontab_log.txt" to get into Excel format

#-------------notes to self--------------------
#Use chmod +x filename.sh to make a shell file executable
#https://data36.com/web-scraping-tutorial-episode-1-scraping-a-webpage-with-bash/   <----- Website with instructions
