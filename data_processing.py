from PIL import Image, ImageEnhance
from ephem import readtle, degree

def get_pixels_of_class(image):
    pixels = image.getdata()
    black_thresh = 150
    cloud_thresh = 600

    total_dark_pix = 0
    total_cloud_pix = 0

    for pixel in pixels:
        pixel_size = sum(pixel)
        if (pixel_size < black_thresh):
            total_dark_pix += 1
        elif pixel_size > cloud_thresh:
            total_cloud_pix += 1

    return total_dark_pix, total_cloud_pix


def get_pct_clouds(filename):
    # Open locally stored image
    image = ImageEnhance.Contrast(Image.open(f"./clouds/raw/{filename}")).enhance(2)

    # Compute total white pixels from image array
    total_dark_pix, total_cloud_pix = get_pixels_of_class(image)
    total_pix = (image.width * image.height) - total_dark_pix

    # Compute % of image which is white
    pct_cloud_of_image = round((total_cloud_pix / total_pix) * 100, 2)

    return pct_cloud_of_image


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

def calcLatLong():
    with open('stations.txt', 'r') as file:
        lines = file.readlines()

    name = lines[0]
    line1 = lines[1]
    line2 = lines[2]

    iss = readtle(name, line1, line2)
    iss.compute()

    lat = iss.sublat / degree
    long = iss.sublong / degree

    return lat, long
