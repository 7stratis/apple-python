import subprocess

data1 = subprocess.Popen(['sudo', '-nl'], stdout = subprocess.PIPE)
output1=data1.communicate()
if output1==('', None):
	print "Please run the script with sudo"
	exit()

hostname=raw_input("Enter the hostname: ")
LocalHostName=raw_input("Enter the LocalHostName: ")
ComputerName=raw_input("Enter the ComputerName: ")

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
