# uArm Swift Pro - Python Library Example
# Created by: Richard Garsthagen - the.anykey@gmail.com
# Modified by: jfdzar 
# V0.1 - June 2017 - Still under development

import uArmRobot
import time
import serial

#Configure Serial Port
serialport = 'COM7'          # for windows 
#serialport = "/dev/ttyACM0"  # for linux like system

# Connect to uArm 
myRobot = uArmRobot.robot(serialport)
myRobot.debug = False   # Enable / Disable debug output on screen, by default disabled
myRobot.connect()

# Set mode to Normal
myRobot.mode(0)   
# Get actual Position
print(myRobot.get_position())


#Go to Test Position
myRobot.goto(200,0,100,30000)
#Change the acceleration and move to test acceleartion
myRobot.set_acceleration(300,300)
myRobot.goto(200,150,100,30000)
myRobot.goto(200,-150,100,30000)
#Change the acceleration and move to test acceleartion
myRobot.set_acceleration(200,200)
myRobot.goto(200,150,100,5000)
myRobot.goto(200,-150,100,5000)
myRobot.goto(200,0,100,5000)

#Print Test
myRobot.mode(1) 
z = 100
speed = 5000
for i in range(1,4):
    myRobot.laser_goto(200,0,z,speed)
    myRobot.laser_goto(200,50,z,speed)
    myRobot.laser_goto(210,50,z,speed)
    myRobot.laser_goto(210,0,z,speed)
myRobot.mode(0)

# Send move command, but continue program
myRobot.async_goto(200,150,250,3000)
while myRobot.moving:
    print ("Waiting to complete move")
    time.sleep(0.5)

#Set Normal Mode go to Home Position and disconnect the robot
myRobot.mode(0)
myRobot.goto(100,0,40,5000)
print('Disconnecting Robot')
myRobot.disconnect()