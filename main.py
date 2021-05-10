import os

try:
    import threading,paramiko,time,json,sys
except:
    print("Installing requirments ...")
    os.system("py -m pip install -r requirments.txt")
    import threading,paramiko,time,json,sys
    
config = json.loads(open("config.json","r").read())
out = []
found = False

done = 0

def addOut(data):
    global out
    out.append(data)
    
    ot = open(config["log_file_name"],"w")
    for a in out:
        ot.write(a+"\n")
    ot.close()
    lastOut = out

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    
    return rightMin + (valueScaled * rightSpan)

def loadingBar(val,pretext,text,loadBarLength):
    global maxThreads
    value = translate(val,0,maxThreads,0,loadBarLength)
    value = int(value)
    
    percentage = int(val/(maxThreads/100))
    
    sys.stdout.write("\r" + str(pretext) + "[" + "#"*value + "-"*(loadBarLength-value) + "] " + str(percentage) + "% "+ text + str(val))
    sys.stdout.flush()
    
def ping(host):
    global out,found,done
    
    ot = os.popen('ping -n 1 ' + host).read()
    
    if "(0% loss)" in ot and not "Destination host unreachable" in ot and found == False:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            if config["ssh"]["password"] != "":
                ssh.connect(host, username=config["ssh"]["username"], password=config["ssh"]["password"])
            else:
                ssh.connect(host, username=config["ssh"]["username"])
                
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("hostname -I")
            
            if config["autoSSH"]:
                os.system("putty.exe "+host+" -l pi -pw raspberry")
                
            addOut("Successfuly connected to: " + host)
        except Exception as err:
            addOut("Error at host: " + host + " => " + str(err))
            pass
    
    done += 1
    
maxThreads = 254
loadBarLength = 20

sys.stdout.write("Starting threads:\n")

for a in range(maxThreads):
    loadingBar(a+1," "," Active threads: ",20)
    
    thread = threading.Thread(target=ping,args=(("192.168.1."+str(a+1)),))
    thread.start()

sys.stdout.write("\nProgress: \n")

while True:
    
    loadingBar(done," "," Done threads: ",20)
    
    if done == maxThreads:
        loadingBar(done," "," Done threads: ",20)
        break
    
    time.sleep(0.1)
   