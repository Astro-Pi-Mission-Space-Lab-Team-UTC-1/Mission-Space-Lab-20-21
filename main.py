from data_processing import get_pct_clouds, calcLatLong, calcOktas
import shutil
import csv
import os

from picamera import PiCamera
from time import sleep



def start():
    camera = PiCamera()
    camera.resolution = (1920, 1080) 

    for i in range(3*60):
        camera.start_preview()
        sleep(3)
        camera.capture('./clouds/raw/cloud_{i}' % i)
        camera.stop_preview()

        if i % 25 == 0:
            csvWrite()




def collectData():
    data = []

    images = os.listdir('./clouds/raw')

    for filename in images:
        temp = {}

        temp['name'] = filename

        ptc = get_pct_clouds(filename)
        temp['% of clouds'] = ptc

        lat, long = calcLatLong()
        temp['latitude'] = lat
        temp['longitude'] = long

        temp['cloud cover (oktas)'] = calcOktas(ptc)

        data.append(temp)
    
    shutil.move('./clouds/raw', './clouds/processed')

    return data


def csvWrite():

    with open('data.csv', 'a+') as csv_file:
        fields = ['name', '% of clouds', 'latitude', 'longitude', 'cloud cover (oktas)']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fields)

        csv_writer.writeheader()

        csv_writer.writerows(collectData())

    print('Done writing to data.csv 🎉')