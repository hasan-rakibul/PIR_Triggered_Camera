from gpiozero import MotionSensor       #impport module to use PIR motion sensor
from picamera import PiCamera           #impport module to use the camera module
from datetime import datetime

pir =MotionSensor(4)    #PIR sensor connected to pin GPIO 4
today=datetime.now()    #takes the current time
time = int(today.strftime("%H"))    #extract only hour from current time

while time>8 and time<17 :      #time range to capture
    pir.wait_for_motion()       #Upto motion 
    print("MOtion Detected")
    today=datetime.now()        #takes the current time
    time = int(today.strftime("%H"))    #extract only hour from current time
    camera = PiCamera()         #Create a PiCamera Object
    camera.rotation=180         #Rotate the image if needed
    camera.capture('/home/pi/Desktop/image/'+str(today) + '.png')       #Capture the image and store it
    camera.close()              #Close the Camera 
    
