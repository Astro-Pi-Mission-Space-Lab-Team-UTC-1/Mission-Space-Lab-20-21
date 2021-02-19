from data_processing import get_pct_clouds, calcLatLong, calcOktas
import shutil, csv, os,signal, datetime, sys
from picamera import PiCamera
from time import sleep

# Main function
def run(hours, minutes):
    setupFolders()
    csvCreate()

    # Initializes PiCamera instance
    camera = PiCamera()
    camera.resolution = (1920, 1080)

    # Loop runs for 3 hours
    i = 0
    while True:
        d = datetime.datetime.now()


        if d.hour == hours and d.minute == minutes:
            # processes
            csvWrite()
            print('Done! ✅')
            os.kill(os.getppid(), signal.SIGKILL)
            sys.exit()
        else:
            camera.start_preview()
            sleep(5)
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

    # Returns array of filenames in the directory
    images = os.listdir('./clouds/raw')

    # Loops through all the file names
    for filename in images:
        temp = []

        # Adds name of image to array
        temp.append(filename)

        # Calculates percentage of cloud for the image
        ptc = get_pct_clouds(filename)
        # Adds ptc to array
        temp.append(ptc)

        # Calculates the current latitude and longitude
        lat, long = calcLatLong()
        # Adds latitude and longitude to array
        temp.append(lat)
        temp.append(long)

        # Calculate and append the cloud coverage (okta) to array
        temp.append(calcOktas(ptc))

        # Moves file after processing it
        shutil.move(f'./clouds/raw/{filename}', f'./clouds/processed/{filename}')

        data.append(temp)

    return data

# Writes empty data01.csv
def csvCreate():

    with open('data01.csv', 'w+') as csv_file:
        fields = ['name', '% of clouds', 'latitude', 'longitude', 'cloud cover (oktas)']

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(fields)

    print('data01.csv file created! ✅')

# Appends data to data01.csv
def csvWrite():

    with open('data01.csv', 'a+') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerows(collectData())

    print('Written data to data01.csv ✅')

# Run program for specified time
# run(hours, minutes)
run(2, 58)
