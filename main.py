import threading,os,paramiko

out = open("out.txt","w")

found = False

def ping(host):
    global out,found
    
    ot = os.popen('ping -n 1 ' + host).read()
    
    if "(0% loss)" in ot and not "Destination host unreachable" in ot and found == False:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username="pi", password="raspberry")
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("hostname -i")
            os.system("putty.exe "+host+" -l pi -pw raspberry")
            print(host)
            out.write(str(host))
            exit()
        except Exception as err:
            print(err)
        
for a in range(254):
    thread = threading.Thread(target=ping,args=(("192.168.1."+str(a+1)),))
    thread.start()
    
input()