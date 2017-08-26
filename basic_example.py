# uArm Swift Pro - Python Library Example
# Created by: Richard Garsthagen - the.anykey@gmail.com
# V0.1 - June 2017 - Still under development

import uArmRobot
import time
import serial

#Configure Serial Port
serialport = 'COM7'          # for windows 
#serialport = "/dev/ttyACM0"  # for linux like system

# Connect to uArm 
myRobot = uArmRobot.robot(serialport)
myRobot.debug = True   # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal

time.sleep(1)
myRobot.get_position()



myRobot.mode(1)
time.sleep(2)


myRobot.set_acceleration(300,300)
myRobot.goto(200,0,100,30000)
myRobot.goto(200,150,100,30000)
myRobot.goto(200,-150,100,30000)

myRobot.set_acceleration(200,200)
myRobot.goto(200,150,100,5000)
myRobot.goto(200,-150,100,5000)
myRobot.goto(200,0,100,5000)


myRobot.mode(0)
myRobot.goto(100,0,40,5000)

time.sleep(5)

print('Disconnecting Robot')
myRobot.disconnect()

exit()
z = 100
speed = 50000
for i in range(1,7):
    myRobot.laser_goto(200,0,z,speed)
    myRobot.laser_goto(200,50,z,speed)
    myRobot.laser_goto(210,50,z,speed)
    myRobot.laser_goto(210,0,z,speed)

z = 120
for i in range(1,7):
    myRobot.laser_goto(200,0,z,speed)
    myRobot.laser_goto(200,50,z,speed)
    myRobot.laser_goto(210,50,z,speed)
    myRobot.laser_goto(210,0,z,speed)
    
myRobot.mode(0)
myRobot.goto(100,0,40,5000)

time.sleep(5)

print('Disconnecting Robot')
myRobot.disconnect()

exit()

# Turn on the pump
myRobot.pump(True)

# Send move command, but continue program
myRobot.async_goto(200,150,250,3000)
while myRobot.moving:
    print ("Waiting to complete move")
    time.sleep(0.5)

#Turn off the pump
myRobot.pump(False)

# Send move command, but continue program
myRobot.async_goto(200,0,100,6000)
while myRobot.moving:
    print ("Waiting to complete move")
    time.sleep(0.5)


time.sleep(5)

#Disconnect serial connection
myRobot.disconnect()




