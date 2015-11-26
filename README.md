# SpheroOllie-python
**Sphero's Ollie** 

Now even better with a python API library!

Use "sudo hcitool lescan" to find Ollie's MAC address 
input it at "`deviceAddress =`" (line 244) in the Sphero class in Ollie_driver.py

**

***Included Scripts:***

**
**OllieTest.py**
A simple program that connects to Ollie and flashes the internal RGB LED red to green to blue. You can take it a step further and add `ollie.roll` commands to make him move using the API. 

**OlliejoyDrive.py**
*requires PyGame library* 

Allow you to drive Ollie with a joystick/gamepad.
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

