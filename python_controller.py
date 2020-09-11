import pyvjoy
import socket, pickle
import threading
device_num=0
print_lock = threading.Lock() 
HOST = 'YourIP'
PORT = 32976 #this is just a random port i tried
def runThread(conn,j,s):
    print("inside thread ",conn)
    
    while(True):
        try:
            #print_lock.acquire()
            data = conn.recv(200)
            #print_lock.release()
            data2= pickle.loads(data)
            j.data=data2
            j.update()
            data_string =pickle.dumps(data2[1])
            conn.send(data_string)
        except :
            j.reset()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("connction for ",s)
    s.listen(3)
except:
    print("Socket connection problem")
j1=[]
global conn,addr
while True:
    if device_num<2:
        try:
            j1.append(pyvjoy.VJoyDevice(device_num+1))
        except:
            print("Vjoy Connection error",device_num)
            break
    try:
        conn, addr = s.accept()
    except:
        print("Connection Error",PORT,device_num,HOST)
        continue
    print ('Connected by', addr)
    thread=threading.Thread(target=runThread,args=(conn,j1[device_num],s))
    thread.daemon = True       
    thread.start()
    
    device_num+=1
    print("Thread working")
    #runThread(conn,j[device_num])

conn.close()
print ('Data received from client')