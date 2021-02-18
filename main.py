from data_processing import get_pct_clouds, calcLatLong, calcOktas
import shutil, csv, os,signal, datetime, sys
from picamera import PiCamera
from time import sleep 



def start(hours):
    camera = PiCamera()
    camera.resolution = (1920, 1080) 

    i = 0
    while True:
        d = datetime.datetime.now()
        

        if d.hour == hours:
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

        shutil.move(f'./clouds/raw/{filename}', f'./clouds/processed/{filename}')
    
    

    return data


def csvWrite():

    with open('data.csv', 'a+') as csv_file:
        fields = ['name', '% of clouds', 'latitude', 'longitude', 'cloud cover (oktas)']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fields)

        csv_writer.writeheader()

        csv_writer.writerows(collectData())

    print('Written data to data.csv 🎉')


start(3)