import subprocess
# import os

# import subprocess
# test = subprocess.Popen(["scutil","--set","HostName","oyo"], stdout=subprocess.PIPE)
# import os
# os.system("softwareupdate -l")


data1 = subprocess.Popen(['sudo', '-nl'], stdout = subprocess.PIPE)
output1=data1.communicate()
# ('', None)
if output1==('', None):
	# print True
	exit()
else:
	print False
	# print output1

data = subprocess.Popen(['softwareupdate', '-l'], stdout = subprocess.PIPE)
output = data.communicate()
print output[0]
# print output

c=raw_input("If you want to install all the updates?")
if(c=="Y" or c=="y"):
	data1 = subprocess.Popen(['softwareupdate', '-ia'], stdout = subprocess.PIPE)
	output1 = data1.communicate()
	exit()
else:
	hostname=raw_input("enter the hostname")
	LocalHostName=raw_input("enter the LocalHostName")
	ComputerName=raw_input("enter the ComputerName")

	test = subprocess.Popen(["scutil","--set","HostName",hostname], stdout=subprocess.PIPE)
	outputm = test.communicate()[0]
	print outputm
	test = subprocess.Popen(["scutil","--set","ComputerName",ComputerName], stdout=subprocess.PIPE)
	outputm = test.communicate()[0]
	print outputm
	test = subprocess.Popen(["scutil","--set","LocalHostName",LocalHostName], stdout=subprocess.PIPE)
	outputm = test.communicate()[0]
	print outputm

	exit()

	
# coool="""{}""".format(output[0])
# print coool
# formatted_output = output.replace('\\n', '\n').replace('\\t', '\t')
# print formatted_output
# print output
