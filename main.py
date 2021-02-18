from data_processing import get_pct_clouds, calcLatLong, calcOktas
import shutil, csv, os,signal, datetime, sys
from picamera import PiCamera
from time import sleep 



def run(hours):
    setupFolders()
    csvCreate()

    camera = PiCamera()
    camera.resolution = (1920, 1080) 
    
    # Loop runs for 3 hours
    i = 0
    while True:
        d = datetime.datetime.now()

        if d.hour == hours:
            csvWrite()
            print('Done! ✅')
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


# Create 'clouds' folder if it doesn't exist
def setupFolders():
    if os.path.exists('./clouds') != True:
        os.mkdir('./clouds')
        os.mkdir('./clouds/raw')
        os.mkdir('./clouds/processed')

        print('Cloud images directory setup ✅')
    else:
        print('Clouds directory already setup! ✅')


# Collects an array of information to write to csv
def collectData():
    data = []

    images = os.listdir('./clouds/raw')

    for filename in images:
        temp = []

        temp.append(filename)

        ptc = get_pct_clouds(filename)
        temp.append(ptc)

        lat, long = calcLatLong()
        temp.append(lat)
        temp.append(long)

        temp.append(calcOktas(ptc))

        # Moves file after generating data from it
        shutil.move(f'./clouds/raw/{filename}', f'./clouds/processed/{filename}')

        data.append(temp)    

    return data

# Writes empty data.csv
def csvCreate():

    with open('data.csv', 'w+') as csv_file:
        fields = ['name', '% of clouds', 'latitude', 'longitude', 'cloud cover (oktas)']

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(fields)

    print('data.csv file created! ✅')

# Appends data to data.csv
def csvWrite():

    with open('data.csv', 'a+') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerows(collectData())

    print('Written data to data.csv ✅')

# Starts program
run(3)
