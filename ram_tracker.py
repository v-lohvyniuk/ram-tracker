import platform,socket,re,uuid,json,psutil,logging, time, sys
from datetime import datetime

filename = datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + "_performance.log"
logging.basicConfig(filename=filename,level=logging.DEBUG)


delay = 1
if len(sys.argv) > 1:
	delay = int(sys.argv[1])
	
	
def getSystemInfo():
	info={}
	info['datetime']= datetime.now().strftime("%H:%M:%S")
	info['cpu']= psutil.cpu_percent()	
	info['ram']=str(100 - round(psutil.virtual_memory().free / psutil.virtual_memory().total * 100))+" %"
	return json.dumps(info)



logging.info(getSystemInfo())
print(getSystemInfo())

while True:
	system_info = getSystemInfo()
	print(system_info)
	logging.info(system_info)
	time.sleep(delay)