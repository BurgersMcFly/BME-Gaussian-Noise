#add noise to dataset
import numpy as np
import cv2
import glob 
import os

mean = 0
var = 50
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (720, 1280))

#Directory containing the images. Can replace "jpg" with whatever format your images are in.
path = "testimgs/*jpg"

#Create a folder for the noisy images to be saved in.
os.mkdir("testimgs/Noise1")

#noise
for image in glob.glob('testimgs/*.jpg'):
    img = cv2.imread(image)
    noisy_image = np.zeros(img.shape, np.float32)

    if len(img.shape) == 2:
        noisy_image = img + gaussian
    else:
        noisy_image[:, :, 0] = img[:, :, 0] + gaussian
        noisy_image[:, :, 1] = img[:, :, 1] + gaussian
        noisy_image[:, :, 2] = img[:, :, 2] + gaussian

        cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
        noisy_image = noisy_image.astype(np.uint8)

#Save noisy images
        basename = os.path.splitext(os.path.basename(image))[0]
        cv2.imwrite(os.path.join('testimgs/Noise1',f'{basename}.jpg'), noisy_image)
