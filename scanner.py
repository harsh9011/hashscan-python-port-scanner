import socket
import threading
import time


target = input("enter target : ")
print("starting HashScan v1.0")
print("Scanning target : "+ target)
start_time = time.time()
def scan_port(port):
    try:
        
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))

        if result == 0:
            print("port", port ," is OPEN")

        s.close()
    except:
        pass

start_time = time.time()

threads = []


for port in range(1,1025):
    thread = threading.Thread(target=scan_port,args=(port,))
    thread.start()
    threads.append(thread)


for thred in threads:
    thread.join()
    end_time = time.time()



print("Scan Completed in : ", end_time - start_time , "Seconds")


