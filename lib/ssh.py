import paramiko



def ssh_execmd(host,passwd,cmd):
    transport = paramiko.Transport((host, 22))
    transport.connect(username='root', password=passwd)
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.read()
    transport.close()
    return  result