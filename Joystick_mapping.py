import pygame
import socket, pickle

import sys
from ctypes import *


from pyvjoy.constants import *
from pyvjoy.exceptions import *
import pyvjoy._sdk
from ctypes import wintypes
pygame.init()

import time
 
def main(): 
    i=0
    avg=0  
    print("hreh")
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Joystick Testing / XBOX360 Controller")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    joysticks = []
    clock = pygame.time.Clock()
    keepPlaying = True
    print("here")
    # for al the connected joysticks
    for i in range(0, pygame.joystick.get_count()):
        print(pygame.joystick.Joystick(i).get_name())
    joysticks.append(pygame.joystick.Joystick(0))
    
    joysticks[-1].init()
    
    print ("Detected joystick ",joysticks[-1].get_name(),"'")
    data=pyvjoy._sdk.CreateDataStructure(joysticks[0].get_id())
    print(type(data))
    eventVal=0
    ev=0
    ax=0
    MAX_VJOY = 32767
    HOST = 'InsertIP'
    PORT = 32976
    # Create a socket connection.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print(s)
    while keepPlaying:
        pt=False
        clock.tick(60)
        for event in pygame.event.get():
            
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print ("Escape key pressed, exiting.")
                keepPlaying = False
                pt=True
            
            elif event.type == pygame.JOYAXISMOTION:
                print ("Joystick '",joysticks[0].get_name(),"' value",event.value,"axis",event.axis,"motion.")
                ev=(event.value+1)/2
                if event.axis==0:
                    data.wAxisX=int(ev * MAX_VJOY)
                elif event.axis==1:
                    data.wAxisY=int(ev * MAX_VJOY)
                elif event.axis==2:
                    data.wAxisXRot=int(ev * MAX_VJOY)
                elif event.axis==3:
                    data.wAxisYRot=int(ev * MAX_VJOY)
                '''
                self.j.data.wAxisX = int(X * self.MAX_VJOY)
                self.j.data.wAxisY = int(Y * self.MAX_VJOY)
                self.j.data.wAxisZ = int(Z * self.MAX_VJOY)
                self.j.data.wAxisXRot = int(XRot * self.MAX_VJOY)
                '''
                pt=True
                
            elif event.type == pygame.JOYBUTTONDOWN:
                print ("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"down.")
                
                eventVal+=(2**event.button)
                print(eventVal)
  
              
            elif event.type == pygame.JOYBUTTONUP:
                print ("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"up.")
                    
                eventVal-=(2**event.button)
                print(eventVal)
            elif event.type == pygame.JOYHATMOTION:
                x,y=event.value
                if x==0 and y==0:
                    data.bHats=-1
                    continue
                
                if y==1:
                    data.bHats=0
                elif y==-1:
                    data.bHats=2
                elif x==1:
                    data.bHats=1
                elif x==-1:
                    data.bHats=3                 
                print ("Joystick '",joysticks[event.joy].get_name(),"' hat",event.hat," moved.",event.value,data.bHats)
        # Create an instance of ProcessData() to send to server.
        data.lButtons=eventVal
        # Pickle the object and send it to the server
        ts = time.time()
        data_string = pickle.dumps([data,ts])
        s.send(data_string)
        
        data1=s.recv(1024)
        
        date=pickle.loads(data1)
        
        
        if i<10:
            avg +=time.time()-date
            i+=1
            print(time.time()-date)
        if i==10:
            print(avg,avg/i)
            i+=1
        if pt:
            avg +=time.time()-date
            i+=1
            print(time.time()-date)
            print(avg/i)
            pt=False
            
        
        screen.blit(background, (0, 0))
        pygame.display.flip()
    s.close()




main()
pygame.quit()
