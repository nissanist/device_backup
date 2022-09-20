#!/usr/bin/python3
# Backup Cisco config
 
# import modules needed and set up ssh connection parameters
import paramiko
import datetime
user = 'test'
secret = 'test'
port = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
# define variables
time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
#infilepath = "c:\\Users\\nissan\\Downloads\\"
outfilepath = "/home/backup_config/"
devicelist = "ip_cisco_dev.txt"
 
# open device file
input_file = open( devicelist, "r")
iplist = input_file.readlines()
input_file.close()
 
# loop through device list and execute commands
for ip in iplist:
    ipaddr = ip.strip()
    ssh.connect(hostname=ipaddr, username=user, password=secret, port=port)
    #ssh.exec_command('terminal length 0')
    #stdin, stdout, stderr = ssh.exec_command('show run | sec hostname')
    #dev_name = stdout.readlines()
    #name = dev_name[1]

    stdin, stdout, stderr = ssh.exec_command('show run')
    config_bk = stdout.readlines()

    outfile = open(outfilepath + ipaddr + "_" + time_now, "w")
    for char in config_bk:
        outfile.write(char)
    ssh.close()
    outfile.close()