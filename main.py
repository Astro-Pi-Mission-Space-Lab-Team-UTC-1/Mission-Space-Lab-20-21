from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from scipy import stats
from oktas import calcOktas


def white():
    wc = 0

    # Open locally stored image
    image = Image.open("clouds/cloud4.png")

    temp = ImageEnhance.Contrast(image).enhance(100).convert("1")

    temp.save("sadf.jpeg")

    # Image as numpy array
    np_image = np.array(temp)

    # Compute total white pixels from image array
    total_white_pix = np.sum(np_image == True)
    total_pix = np.size(np_image)

    # Compute % of image which is white
    pct_white_of_image = round((total_white_pix / total_pix) * 100, 2)

    print(f"total pixels: {total_pix}")
    print(f"total white pixels: {total_white_pix}")
    print(f"% white of image: {pct_white_of_image}%")


white()
