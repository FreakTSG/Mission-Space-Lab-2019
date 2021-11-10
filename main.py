from sense_hat import SenseHat
from logzero import logger, logfile
from ephem import readtle, degree
from time import sleep
from datetime import datetime, timedelta
from random import choice
import random
import datetime
import os
import csv
sense = SenseHat()
dir_path = os.path.dirname(os.path.realpath(__file__))
logfile(dir_path + "/AEBSpace.log")
def create_csv_file(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Temperature", "Pressure", "Pitch", "Roll", "Yaw","Acceleration_x", "Acceleration_y","Acceleration_z")
        writer.writerow(header)
def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
def get_latlon():
    iss.compute()
    long_value = [float(i) for i in str(iss.sublong).split(":")]
    if long_value[0] < 0:
        long_value[0] = abs(long_value[0])
        cam.exif_tags['GPS.GPSLongitudeRef'] = "W"
    else:
        cam.exif_tags['GPS.GPSLongitudeRef'] = "E"
    cam.exif_tags['GPS.GPSLongitude'] = '%d/1,%d/1,%d/10' % (long_value[0], long_value[1], long_value[2]*10)
    lat_value = [float(i) for i in str(iss.sublat).split(":")]
    if lat_value[0] < 0:
        lat_value[0] = abs(lat_value[0])
        cam.exif_tags['GPS.GPSLatitudeRef'] = "S"
    else:
        cam.exif_tags['GPS.GPSLatitudeRef'] = "N"
    cam.exif_tags['GPS.GPSLatitude'] = '%d/1,%d/1,%d/10' % (lat_value[0], lat_value[1], lat_value[2]*10)
    return (iss.sublat / degree, iss.sublong / degree)

data_file = dir_path + "/data.csv"
create_csv_file(data_file)
start_time = datetime.datetime.now()
now_time = datetime.datetime.now()

while (now_time < start_time + timedelta(minutes=178)):
    try:
        humidity = round(sense.humidity, 4)
        pressure = round(sense.get_pressure(),4)
        o = sense.get_orientation()
            Pitch = o["pitch"]
            Roll = o["roll"]
            Yaw = o["yaw"]
        acceleration = sense.get_accelerometer_raw()
            Acceleration_x = x
            Acceleration_y = y
            Acceleration_z = z
        lat, lon = get_latlon()
        data = (datetime.now(), humidity, Pressure, Pitch, Roll, Yaw, Acceleration_x, Acceleration_y,Acceleration_z, lat, lon)
        add_csv_data(data_file, data)
        now_time = datetime.now()
    except Exception as e:
        logger.error('{}: {})'.format(e.__class__.__name__, e))
        
while (now_time < start_time + timedelta(minutes=178)):
g = [0,50,0]
o = [0,0,0]
y = [100,100,0]
img1 = [
g,g,g,g,g,g,g,g,
o,g,o,o,o,o,g,o,
o,o,g,o,o,g,o,o,
o,o,o,g,g,o,o,o,
o,o,o,g,g,o,o,o,
o,o,g,o,o,g,o,o,
o,g,y,y,y,y,g,o,
g,y,y,y,y,y,y,g,
]
img2 = [
g,g,g,g,g,g,g,g,
o,g,o,o,o,o,g,o,
o,o,g,o,o,g,o,o,
o,o,o,g,g,o,o,o,
o,o,o,g,g,o,o,o,
o,o,g,y,y,g,o,o,
o,g,y,y,y,y,g,o,
g,y,y,y,y,y,y,g,
]
img3 = [
g,g,g,g,g,g,g,g,
o,g,y,y,y,y,g,o,
o,o,g,y,y,g,o,o,
o,o,o,g,g,o,o,o,
o,o,o,g,g,o,o,o,
o,o,g,y,y,g,o,o,
o,g,y,y,y,y,g,o,
g,y,y,y,y,y,y,g,
]
def active_status():
sense = SenseHat()
sense.set_pixels(img1)
sense.flip_h()
sleep(5)
sense.set_pixels(img2)
sense.flip_v()
sleep(5)
sense.set_pixels(img3)
sense.flip_h()
while True:
    sleep(2)
    active_status()
    orientation = [0,90,270,180]
    rot = random.choice(orientation)
    sense.set_rotation(rot)
while True:
    sleep(5)
    active_status()
    sleep(5)
    active_status()
    now_time = datetime.datetime.now()