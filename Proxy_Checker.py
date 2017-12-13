
#Networking
import urllib.request,urllib.error, socket

#Misc
import time
import os



#Global Variables
test_url = "http://www.google.com"
socket.setdefaulttimeout(1)
ok_msg = "Working: "
fail_msg = "FAIL: "
working_proxies = []
count = 0

#Proxylist
with open(os.path.join(os.path.realpath('.'), 'proxylist.txt')) as f:
	proxylist = f.read().splitlines()

#statistics
start_time = time.time()



def non_working(pip):
	try:
		opener = urllib.request.build_opener(urllib.request.ProxyHandler({'http' : pip}))
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		urllib.request.install_opener(opener)
		req = urllib.request.Request(test_url)
		sock = urllib.request.urlopen(req)
	except urllib.error.HTTPError as e:
		print ('Error code', e.code)
		return e.code
	except Exception as detail:
		return 1
	return 0
	

for item in proxylist:
	if non_working(item):
		print(fail_msg, item)
	else:
		working_proxies.append(item)
		print(ok_msg, item)

#statistics
end_time = time.time()
total_time = end_time - start_time

file = open(os.path.join(os.path.realpath('.'), 'working.txt'), 'w+')
for item in working_proxies:	
	file.write("%s\n" % item)
file.close()


print("Total Time:", total_time)
