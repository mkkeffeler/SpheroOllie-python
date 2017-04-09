# SpheroOllie-python
A library of functions to be used with the Sphero Ollie!

#Setup
Run the following commands in your terminal. You must be running this on a computer that has Bluetooth LE (Different from standard bluetooth)
'sudo apt-get install python-pip libglib2.0-dev build-essential git'
'sudo pip install bluepy'
'git clone https://github.com/mkkeffeler/SpheroOllie-python'
'git checkout patch_branch'

#Getting Ready
Use 'sudo hcitool lescan' to find Ollie's MAC address 

input this device address "`deviceAddress =`" (line 244) in the Sphero class in Ollie_driver.py

Currently, Ollietest.py allows you to direct your Ollie where to go using the I J K and L keys. The G key is used to end the program. 


***Included Scripts:***
**
**OllieTest.py**
A simple program that connects to Ollie and flashes the internal RGB LED red to green to blue. You can take it a step further and add `ollie.roll` commands to make him move using the API. 

**OlliejoyDrive.py**
*requires PyGame library* 

Allows you to drive Ollie with a joystick/gamepad.
Shows on screen feedback of analog stick as well as speed and heading
Currently setup for a Xbox 360 controller.

 - Left analog stick controls Ollie's movement, much the like app!   
 - Holding the Left trigger stops Ollie.
 - Tapping the Left bumper changes Ollie's heading - used to calibration.   
 -  Holding the Right bumper turns on Ollie's blue 'tail light' to aid in calibration.

> Adapted the sphero driver library from:
> https://github.com/mmwise/sphero_ros/tree/groovy-devel/sphero_driver/src/sphero_driver
> 
> Used the bluetooth 'stuff' from:
> https://gist.github.com/ali1234/5e5758d9c591090291d6

**TODO:**
Tie in the btle handleNotifcations to Sphero response API
    

 - getting sensor info, command responses, etc. back from Ollie

