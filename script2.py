import subprocess

data1 = subprocess.Popen(['sudo', '-nl'], stdout = subprocess.PIPE)
output1=data1.communicate()
if output1==('', None):
	print "Please run the script with sudo"
	exit()

#data = subprocess.Popen(['softwareupdate', '-l'], stdout = subprocess.PIPE)
#output = data.communicate()
#print output[0]
#if(output!=('Software Update Tool\n\nFinding available software\n', None)):
	#print("Software Updates available")
	#c=raw_input("Do you want to install the Software Updates? [Y/n]?: ")
	#if(c=="Y" or c=="y"):
		#data1 = subprocess.Popen(['softwareupdate', '-ia'], stdout = subprocess.PIPE)
		#output1 = data1.communicate()
		#exit()

hostname=raw_input("Enter the hostname: ")
LocalHostName=raw_input("Enter the LocalHostName :")
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
