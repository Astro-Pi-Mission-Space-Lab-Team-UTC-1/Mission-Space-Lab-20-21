from data_processing import get_pct_clouds, calcLatLong, calcOktas
import shutil, csv, os,signal, datetime, sys
from picamera import PiCamera
from time import sleep 



def run(hours):
    setupFolders()
    csvCreate()

    camera = PiCamera()
    camera.resolution = (1920, 1080) 

    i = 0
    while True:
        d = datetime.datetime.now()

        if d.hour == hours:
            csvWrite()
            print('Done! 🎉')
            os.kill(os.getppid(), signal.SIGKILL)
            sys.exit() 
        else:
            camera.start_preview()
            sleep(3)
            camera.capture(f'./clouds/raw/cloud_{i}.jpg')
            camera.stop_preview()

            if i % 10 == 0:
                csvWrite()
            
            i += 1


def setupFolders():
    os.mkdir('./clouds')
    os.mkdir('./clouds/raw')
    os.mkdir('./clouds/processed')

    print('Cloud images directory setup 🎉')


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

        shutil.move(f'./clouds/raw/{filename}', f'./clouds/processed/{filename}')

        data.append(temp)    

    return data

def csvCreate():

    with open('data.csv', 'w') as csv_file:
        fields = ['name', '% of clouds', 'latitude', 'longitude', 'cloud cover (oktas)']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fields)

        csv_writer.writeheader()

    print('data.csv file created! ✅')


def csvWrite():

    with open('data.csv', 'a+') as csv_file:

        csv_writer = csv.DictWriter(csv_file)

        csv_writer.writerows(collectData())

    print('Written data to data.csv ✅')


run(3)