#add noise
import numpy as np
import cv2
import glob 
import os
mean = 0
var = 1
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (512, 512)) 

path = "/content/messidor2-preprocessed/my_preprocessed/*png"
os.mkdir("/content/messidor2-preprocessed/Noise165")

for image in glob.glob('/content/messidor2-preprocessed/my_preprocessed/*.png'):
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

        basename = os.path.splitext(os.path.basename(image))[0]
        cv2.imwrite(os.path.join('/content/messidor2-preprocessed/Noise165',f'{basename}.png'), noisy_image)