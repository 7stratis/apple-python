import subprocess

data1 = subprocess.Popen(['sudo', '-nl'], stdout = subprocess.PIPE)
output1=data1.communicate()
if output1==('', None):
	print "Please login through sudo user"
	exit()

data = subprocess.Popen(['softwareupdate', '-l'], stdout = subprocess.PIPE)
output = data.communicate()
print output[0]
if(output!=('Software Update Tool\n\nFinding available software\n', None)):
	print("yes updates")
	c=raw_input("If you want to install all the updates?")
	if(c=="Y" or c=="y"):
		data1 = subprocess.Popen(['softwareupdate', '-ia'], stdout = subprocess.PIPE)
		output1 = data1.communicate()
		exit()

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
