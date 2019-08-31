import threading
from multiprocessing import Queue
import time
import socket

print_lock = threading.Lock()

# target = input("enter URL:")
target = 'www.google.com'
ip = socket.gethostbyname(target)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((ip,port))
        with print_lock:
            print('port',port)
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()
        

q = Queue()        
for x in range(100):
     t = threading.Thread(target=threader)
     t.daemon = True
     t.start()

for worker in range(1,65535):
    q.put(worker)
q.join()

start = time.time()