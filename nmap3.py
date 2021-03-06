"""
http://stackoverflow.com/questions/31233780/nameerror-when-using-input-with-python-3-4
The script is written in Python 3
The version of Python that was executed is printed out in the output
If you receive "File "<string>", line 1" when running look at the version information printed.
If it shows other than 3.4 or higher use "python3 nmap3.py"

TO DO
Add vnc-brute
Add vnc-info
Add tn3270-hidden
Add tn3270-screen
Add tsc-brute
Add tso-enum
Add stun-info
Add stun-version
Add sslv2
Example smb arguments
nmap --script=smb-<script>.nse --script-args=smbuser=ron,smbpass=iagotest2k3,smbbasic=1,smbsign=force <host>

Notes:
you should run nmap --script-updatedb if you add any of the non-default scripts listed here.
you can use --script-help to any script to print out its help file I.E. nmap --script-help smb-vuln-cve-2017-7494
you can use --script-trace to output the packets sent and received 
I.E nmap --script ssl-cert,ssl-enum-ciphers --script-trace -p 443,465,993,995 192.168.10.239
nmap cheat sheets
 - https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/
 - https://highon.coffee/blog/nmap-cheat-sheet/
 - https://scadahacker.com/library/Documents/Cheat_Sheets/Hacking%20-%20NMap%20Quick%20Reference%20Guide.pdf

 
Script Usage
If you create a file "ip.txt" in the folder where you run the script it will load the IP address as a default and use
it where an ip address is needed. The file should have one line - the ip address or ip address range to use.

The script will prompt "Are you running Linux" on start up. Enter y for Linux, n for windows. 
On Linux, sudo will be added on scans that require root privliges.

Enter a number from the list of nmap scripts, you will be asked for an IP address or SNMP string if the script requires it.

If an IP address is required you will be prompted to enter one. You can enter an IP address/range or iL and a filename. The file should 
contain a list of hostnames or IP addresses to be scanned, one per line.

For Example, Enter the IP Address or domain name [192.168.10.239]: iL hosts.txt
nmap -vv --script ssl-cert,ssl-enum-ciphers -p 443,465,993,995,3389 iL hosts.txt

The script will output the appropriate nmap command. Copy it and paste into a command line or shell.

"""

import sys; 
import os
import re
ver =  sys.version
pattern = re.compile('\A\d{1}.{1}\d{1}.{1}\d{1}.{1}')
ver = re.findall(pattern,ver)
#print()
print()
ver = ver[0]
print('Running Python version ----> %s' %(ver))
#print()

def readip():
    """
    create a file named ip.txt in the folder where the script is executed.
    In the file enter one ip address or ip address range compatable with
    nmap. 

    The script will read the file and insert the ip address when 
    prompting for an ip address. Simply hit [Enter] to accept the IP. 
    You can override the default by typing in an address.
    This allows you to quickly run several different scans with the same
    IP address.
    """

    try:
        IP = []
        f = open('ip.txt', 'r')
        for line in f:
            IP.append(line)
        f.close
    except: # FileNotFoundError:
        IPAddress = input('Enter the IP Address or domain name: ')
        return IPAddress  

    try:
	    ipsaved = IP[0]
	    ipsaved = ipsaved.strip('\n')
	    if not ipsaved:
	        IPAddress = input('Enter the IP Address or domain name: ')
	    else:
	        IPAddress = input('Enter the IP Address or domain name [%s]: ' %(ipsaved))
	    if not IPAddress:
	        IPAddress = ipsaved

	    return IPAddress  
    except:
        print('\n[!] An Unknown Error Occured or CTRL+C was pressed')


print('''
-1 - Print out script options -- https://nmap.org/book/nse-usage.html, https://nmap.org/book/output-formats-commandline-flags.html
     -----------------
 0 - Download Cisco Configs using SNMP -- https://nmap.org/nsedoc/scripts/snmp-ios-config.html 
     -----------------
 1 - Check Cipher Suites and Certificates using ports 443, 465, 993, 995 and 3389
     https://nmap.org/nsedoc/scripts/ssl-enum-ciphers.html
     https://nmap.org/nsedoc/scripts/ssl-cert.html
     https://nmap.org/nsedoc/scripts/ssl-cert-intaddr.html
     https://nmap.org/nsedoc/scripts/ssl-known-key.html
     -----------------
 2 - Display SSH fingerprint (Host Keys) on an SSh server -- https://nmap.org/nsedoc/scripts/ssh-hostkey.html
     Display the number of algorithms that the target SSH2 server offers. -- https://nmap.org/nsedoc/scripts/ssh2-enum-algos.html
     Checks if an SSH server supports the obsolete and less secure SSH Protocol V1. - https://nmap.org/nsedoc/scripts/sshv1.html
     -----------------
 3 - Performs routing information gathering through Cisco's (EIGRP) Protocol -- https://nmap.org/nsedoc/scripts/broadcast-eigrp-discovery.html
     -----------------
 4 - Display DHCP with the NMAP DHCP-Discover scripts -- https://nmap.org/nsedoc/scripts/dhcp-discover.html 
     https://nmap.org/nsedoc/scripts/broadcast-dhcp-discover.html
     Display IPv6 DHCP with a broadcast discover -- https://nmap.org/nsedoc/scripts/broadcast-dhcp6-discover.html
     -----------------
 5 - Nmap script to find vulnerable Samba devices such as a printer, NAS or any device that allows Windows clients to connect.
     -----------------
 6 - Brute Forcing Telnet with NMAP - Requires files of users and guesses -- https://nmap.org/nsedoc/scripts/telnet-brute.html
     -----------------
 7 - EMS - Environmental Monitoring Systems using scripts from https://github.com/digitalbond/Redpoint#enip-enumeratense
     -----------------
 8 - DNS Broadcast Discover -- broadcast-dns-service-discovery
     -----------------
 9 - Banner Grab using banner-plus from HD Moore -- https://github.com/hdm/scan-tools/blob/master/nse/banner-plus.nse
     -----------------
 10 - NTP Monlist - Pull down NTP server information -- https://nmap.org/nsedoc/scripts/ntp-monlist.html
      NTP INFO - Pull down general NTP information -- https://nmap.org/nsedoc/scripts/ntp-info.html 
     -----------------
 11 - Retrieves the external IP address of a NAT:ed host using the STUN protocol. -- https://nmap.org/nsedoc/scripts/stun-info.html
     -----------------
 12 - DNS Brute - Enumerate DNS hostnames by brute force guessing of common subdomains -- https://nmap.org/nsedoc/scripts/dns-brute.html
     -----------------
 13 - SMB - Various scripts for SMB servers. Make sure you are running nmap 7.50+ as there are a lot of fixes in 7.50.
     -----------------
 14 - SNMP - Is SNMP running on a Windows machine -- https://nmap.org/nsedoc/scripts/snmp-processes.html
      Grab HP printer password using SNMP
     -----------------
 15 - Scan for MS17-010 Wannacry vulnerability -- https://nmap.org/nsedoc/scripts/smb-vuln-ms17-010.html
     -----------------
 16 - MSSQL - Attempt to determine version, config info and check for blank password -- https://nmap.org/nsedoc/scripts/ms-sql-info.html
     -----------------
 17 - Run a fast ping scan on a large IP range. No service detection or port scanning is done.
     -----------------
''')
#
#print()
#
#select the OS. Posix needs sudo appeneded for some scans.
osname = os.name
if osname == "posix":
    sudo = 'sudo'
else:
	sudo = ''

#
#Select a script to run
#Validate that a script number is entered and not an IP Address
nmapTest = input('Input a number to select a script ')
while len(nmapTest) > 2:
	nmapTest = input('Enter a number to select a script not an IP address: ')
	
nmapTest = int(nmapTest)
if nmapTest == -1:
# -1 Help
    print('''
    nmap options
    -iL -> Input from list of hosts/networks. Example  nmap -iL list-of-ips.txt
    -oN -> Save default output to a file. Example nmap -oN outputfile.txt
    -oX -> Save output in XML format. Example nmap -oX outputfile.xml
    -oG -> Save results in a format for grep. Example nmap -oG outputfile.txt
    -oA -> Save in all formats. Example nmap -oA outputfile
     -d -> The debug flag. Levels are 0-9. -d is = to 0, -d9 is highest and shouldn't be used normally.
     -v -> Add verbosity to the output
    -vv -> Add more verbosity to the output
    --script-trace -> All incoming and outgoing communication performed by the script is printed.
    --script-updatedb -> Update the script database. Only needed when new scripts are added
    --script-help=<script name> -> shows a description of what the script does. Example - nmap --script-help smb-vuln-cve-2017-7494
    ''')
#
if nmapTest == 0:
# 0 Download Cisco Configs
    IPAddress = readip()
    SNMP=input('Enter SNMP Private Community String: ')
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('%s  nmap -sU -p 161 --script snmp-ios-config --script-args creds.snmp=%s %s' %(sudo,SNMP,IPAddress))
    print()
    print('%s  nmap -d -sU -p 161 -sC %s <--> Run default scripts against UDP 161' %(sudo,IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 1:
# 1 Checking Server Cipher Suites
    IPAddress = readip()
#    IPAddress=input('Enter the IP Address: ')
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('nmap -vv --script ssl-cert,ssl-enum-ciphers -p 443,465,993,995,3389',IPAddress)
    print()
    print('nmap --script ssl-cert-intaddr -p 443,465,993,995,3389',IPAddress)
    print()
    print('nmap --script ssl-known-key -p 443,465,993,995,3389',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 2:
# 2 Discovering SSH Host Keys
    IPAddress = readip()
#    IPAddress=input('Enter the IP Address: ')
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('nmap --script ssh-hostkey',IPAddress)
    print()
    print('nmap --script ssh2-enum-algos',IPAddress)
    print()
    print('nmap --script sshv1',IPAddress) 
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 3:
    IPAddress = readip()    
#3 EIGRP
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('%s nmap --script=broadcast-eigrp-discovery %s' %(sudo, IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 4:
#4 Troubleshooting DHCP with the NMAP DHCP-Discover script
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('%s nmap -sU -p67 --script broadcast-dhcp-discover' %(sudo))
    print('%s nmap -sU -p67 --script dhcp-discover %s' %(sudo, IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 5:
#5 Troubleshooting IPv6 DHCP discover
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('Download script from https://svn.nmap.org/nmap/scripts/smb-vuln-cve-2017-7494.nse')
    print('nmap --script smb-vuln-cve-2017-7494 -p 445',IPAddress)
    print('nmap --script smb-vuln-cve-2017-7494 --script-args smb-vuln-cve-2017-7494.check-version -p445',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 6:
#6 Brute Forcing Telnet with NMAP
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('nmap -p 23 --script telnet-brute --script-args userdb=users.txt,passdb=pw4.txt',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 7:
#7 BACNET
#https://github.com/digitalbond/Redpoint#enip-enumeratense
    IPAddress = readip()
#    IPAddress=input('Enter the IP Address: ')
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print('Identify and enumerate BACnet devices')
    print()
    print('%s nmap -sU -p 47808 -n --script bacnet-info.nse %s'  %(sudo, IPAddress))
    print('%s nmap -sU -p 47808 -n --script BACnet-discover-enumerate %s'  %(sudo, IPAddress))
    print('%s nmap -sU -p 47808 -n --script BACnet-discover-enumerate --script-args full=yes %s'  %(sudo, IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print('Identify and enumerate CoDeSys V2 controllers')
    print()
    print('nmap -p 1200,2455 --script codesys-v2-discover',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print('Identify and enumerate EtherNet/IP devices from Rockwell Automation and other vendors')
    print()
    print('nmap -p 44818 --script enip-enumerate',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print('Identify and enumerate Niagara Fox devices')
    print()
    print('nmap -p 1911 --script fox-info',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print('Identify and enumerate Schneider Electric Modicon PLCs')
    print()
    print('nmap -p 502 --script modicon-info.nse -sV',IPAddress)
    print()    
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print('Identify and enumerate Omron PLCs')
    print()
    print('nmap -p 9600 --script omrontcp-info',IPAddress)
    print('%s nmap -sU -p 9600 --script omronudp-info %s' %(sudo, IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print('Identify and enumerate PC Worx Protocol enabled PLCs') 	
    print()
    print('nmap -p 1962 --script pcworx-info -sV',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print('Identify and enumerate ProConOS enabled PLCs')
    print()
    print('nmap -p 20547 --script proconos-info -sV',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print('Identify and enumerate Siemens SIMATIC S7 PLCs')
    print()
    print('nmap -p 102 --script s7-enumerate -sV',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')


elif nmapTest == 8:
#8 DNS Broadcast Discover
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('nmap --script=broadcast-dns-service-discovery')
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 9:
#9 Banner Grab
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('nmap -sV --script=banner-plus.nse',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 10:
#10 NTP Monlist
#   NTP INFO
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('%s nmap -sU -p 123 -n --script=ntp-monlist %s' %(sudo, IPAddress))
    print('%s nmap -sU -p 123 --script ntp-info %s' %(sudo, IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 11:
#11 STUN INFO
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('%s nmap -sV -PN -sU -p 3478 --script stun-info %s' %(sudo, IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 12:
#12 DNS Brute
    DNSDomain=input('Enter the DNS Domain Name ')
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('nmap --script dns-brute --script-args dns-brute.threads=10,dns-brute.domain=%s' %(DNSDomain))
    print('nmap --script dns-brute --script-args dns-brute.srv,dns-brute.threads=10,dns-brute.domain=%s,dns-brute.hostlist=<filename>'  %(DNSDomain))
    print('hostlist is a file of hosts strings to try. Defaults to nselib/data/vhosts-full.lst')
    print('http://securityblog.gr/2547/enumerate-dns-hostnames-using-nmap/ for more information')     
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 13:
#13 SMB
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('nmap -p445 --script=smb-os-discovery.nse',IPAddress)
    print('nmap -p445 --script=smb-enum-users.nse',IPAddress)
    print('nmap -F -d --script smb-enum-shares --script-args smbuser=username,smbdomain=domain,smbpass=password',IPAddress)
    print('nmap -p445 --script=smb-brute --script-args=userdb=usernames.txt',IPAddress)
    print('nmap -p445 --script=smb-pwdump --script-args=smbuser=administrator,smbpass=dVd0brx1,rcrack=rcrack,rtable=*.rt',IPAddress)
    print('nmap -p445 --script=smb-brute --script-args=userdb=usernames.txt,passdb=hashes.txt',IPAddress)
    print('nmap -p445 --script=smb-pwdump --script-args=smbuser=administrator,smbhash=dVd0brx1,rcrack=rcrack,rtable=*.rt',IPAddress)
    print('nmap -p445 --script=smb-enum-shares,smb-ls',IPAddress)
    print('nmap -p445 --script=smb-ls --script-args share=c$,path=\\temp',IPAddress)
    print('nmap -p445 --script=smb-mbenum',IPAddress)
    print('nmap -p445 --script=smb-security-mode.nse %s' %(IPAddress))
    print('%s nmap -p U:137,T:139 -sU -sS --script=smb-security-mode.nse %s' %(sudo, IPAddress))
    print('nmap -p445 --script=smbv2-enabled.nse',IPAddress)    
    print('%s nmap -p U:137,T:139 -sU -sS --script=smbv2-enabled.nse %s' %(sudo, IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 14:
#14 SNMP on Windows
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('%s nmap -sU -p 161 --script=snmp-processes %s' %(sudo, IPAddress))
    print('Grab HP Printer Password')
    print('snmpget -v 1 -c public %s .1.3.6.1.4.1.11.2.3.9.1.1.13.0 ' %(IPAddress))
    print('snmpget -v 1 -c public %s .iso.3.6.1.4.1.11.2.3.9.4.2.1.3.9.1.1.0 ' %(IPAddress))
    print('snmpget -v 1 -c internal %s .1.3.6.1.4.1.11.2.3.9.1.1.13.0 ' %(IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 15:
#15 Basic Script Scan
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('%s nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms17-010 %s' %(sudo, IPAddress))
    print()
    print('Include -d for debugging output. This will show more detail about the scan')
    print('%s nmap -d -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms17-010 %s' %(sudo, IPAddress))
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 16:
#16 SQL
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('nmap -sn --script ms-sql-empty-password --script-args mssql.instance-all',IPAddress)
    print('nmap -p 445 --script ms-sql-info',IPAddress)
    print('nmap -p 1433 --script ms-sql-info --script-args mssql.instance-port=1433',IPAddress)
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
#
elif nmapTest == 17:
#17 Rapid Scan of large address space
    IPAddress = readip()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
    print()
    print('nmap -n -sP --min-rate 1000 --max-retries 0 --max-rtt-timeout 100ms --max-scan-delay 0 ',IPAddress) 
    print()
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
