#!/usr/bin/python3.4

import paramiko
import os
import keyring

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
keyfile = os.path.expanduser('~/.ssh/id_rsa')
#password = keyring.get_password('pavelleonov',keyfile)
#password = '81450214768qwe'
#key = paramiko.RSAKey.from_private_key_file(keyfile, password=password)
#pkey = AppropriatePKeySubclassHere.from_private_key_file(keyfile, password=password) 
for i in range(1,261):
	host = 'vh'+ str(i)+'.sweb.ru'
	try:
		ssh.connect(host, port=22, username='pavelleonov', key_filename=keyfile)
		stdin, stdout, stderr = ssh.exec_command('df -h | grep home |awk \'{print $4,$5}\'')
#stdin.write('lol\n')
#stdin.flush()
		data = stdout.readlines()
		data = data[0]
		print('vh{}'.format(i))
		print(data)
		ssh.close()
	except:
		print (host + ' недоступен\n')

