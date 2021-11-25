import ephem
import time
import datetime
from datetime import timedelta
from time import sleep
from ephem import readtle
import logging
import os
import logzero
from logzero import logger
from sense_hat import SenseHat

def display():
    # Define some colours
    g = (0, 255, 0) # Green
    b = (0, 0, 0) # Black
    # Set up where each colour will display
    creeper_pixels = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, b, b, g, g, b, b, g,
        g, b, b, g, g, b, b, g,
        g, g, g, b, b, g, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, g, g, b, g, g
    ]
# Display these colours on the LED matrix
    sense.set_pixels(creeper_pixels)
    return;


dir_path=os.path.dirname(os.path.realpath(__file__)) #path to the raspberry, leading to the files location

#Stuff for the ephem coordinates
name="ISS (ZARYA)"
line1 = "1 25544U 98067A   20044.32408565  .00002939  00000-0  61158-4 0  9991"
line2 = "2 25544  51.6434 246.2798 0004853 268.2335  74.4275 15.49164447212652"
iss = ephem.readtle(name,line1,line2)
sense=SenseHat() #Senehat variable

logzero.logfile(dir_path+"/data.csv") #DATA FILE
formatter = logging.Formatter('%(name)s - %(asctime)-15s - %(levelname)s: %(message)s'); #Formater for files
logzero.formatter(formatter) #Using previous fomater
iss.compute()
Begingtime=time.time()#Seting a begining time
end_time=time.time()+ (60 * 175) #Seting an endtime

while time.time() < end_time: #While cycle until it ends the time (Aprox 175 minutes)
    starttime=time.time() #Another starttime for couning inside the cyle
    print(iss.sublat, iss.sublong) #Showin on commandline the data
    acel=sense.get_accelerometer_raw() #Getting the Accelerometer datta
    tempe=sense.get_temperature() #Getting Temperature
    hum=sense.get_humidity() #Getting HUmidity
    press=sense.get_pressure() #Getting pressure
    gyro=sense.get_gyroscope() #Getting Gyroscope information
    elapsed=round(end_time-time.time())#Elapsed time counter
    elapsed=round(elapsed/60)
    sense.show_message(str(elapsed)) #updating on the minutes left to the program to end
    logger.info("%s,%s,%s,%s,%s,%s,%s",gyro,press,hum,tempe,acel,iss.sublat,iss.sublong)
    #Saving data on the file
    display()
    sleep(60) #Waiting a minute before doing the cyle again
    sense.show_message("AEB")
exit


    
