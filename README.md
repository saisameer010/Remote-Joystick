# Remote-Joystick

This project is used to send the joystick data of client to a host.
more like steam remoteplay (Without Video , will be updated in the next update).
Benifits? it has very low latencey.


## Pre-requisite packages:

pip install pygame 

pip install pyvjoy

## At client:
python and pygame are needed.
just set in the appropriate ipaddress.
run joystickMapping

## At Host:
Install Vjoy  http://vjoystick.sourceforge.net/site/index.php/download-a-install/download
configure the number of devices needed up the number of buttons to 14
If using application like LogmeinHamachi no portforwarding required. 
Else port forward and use the same port in the host program 
run pythonController

for better results and caliberation use X360ce 

For Video currently using 
https://github.com/phoboslab/jsmpeg-vnc



-- Upcoming Video Support --

Tried and tested on 
Fifa 19,
Road Redemption,
Gang Beasts,
Rocket League

