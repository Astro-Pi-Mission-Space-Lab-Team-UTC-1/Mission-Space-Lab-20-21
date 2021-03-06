from PIL import Image, ImageEnhance
from ephem import readtle, degree
from pathlib import Path

dir_path = Path(__file__).parent.resolve()

# Returns number of dark/irrelevent pixels and pixels of a cloud
def get_pixels_of_class(image):
    # Returns a list of tuples
    # Each index of the tuple is in the form [255, 255, 255]
    # Represeting [Red, Green, Blue]
    pixels = image.getdata()

    # Sets threshold values for 'dark' and 'cloud' pixels
    dark_thresh = 150
    cloud_thresh = 600

    # Initiates counter variables
    total_dark_pix = 0
    total_cloud_pix = 0

    # Loops over every pixel in the image
    for pixel in pixels:
        # Sums each value in the tuple
        pixel_size = sum(pixel)

        # Increments total dark/cloud counter variable
        if (pixel_size < dark_thresh):
            total_dark_pix += 1
        elif pixel_size > cloud_thresh:
            total_cloud_pix += 1

    return total_dark_pix, total_cloud_pix

# Returns the percentage of the image which is cloud
def get_pct_clouds(filename):
    # Open locally stored image
    image = ImageEnhance.Contrast(Image.open(f'{dir_path}//clouds/raw/{filename}')).enhance(2)

    # Compute total white pixels from image array
    total_dark_pix, total_cloud_pix = get_pixels_of_class(image)
    total_pix = (image.width * image.height) - total_dark_pix

    # Compute % of image which is white
    pct_cloud_of_image = round((total_cloud_pix / total_pix) * 100, 2)

    return pct_cloud_of_image


# Calculates the cloud coverage in oktas from the percentage
def calcOktas(pct):
  if pct == 0:
    return 0
  elif pct < 18.75:
    return 1
  elif pct < 31.25:
    return 2
  elif pct < 43.75:
    return 3
  elif pct < 56.25:
    return 4
  elif pct < 68.75:
    return 5
  elif pct < 81.25:
    return 6
  elif pct < 100:
    return 7
  elif pct == 100:
    return 8


# Calculates the decimal latitude and longitude of the ISS
def calcLatLong():

    # TLE for ISS
    name = 'ISS (ZARYA)'
    line1 = '1 25544U 98067A   21047.44578741  .00000631  00000-0  19638-4 0  9995'
    line2 = '2 25544  51.6433 219.9227 0002719  22.5068  17.2470 15.48966013269885'

    iss = readtle(name, line1, line2)
    iss.compute()

    # Calculates latitude and longitude in degree form
    lat = iss.sublat / degree
    long = iss.sublong / degree

    # Return latitude and longitude
    return lat, long
