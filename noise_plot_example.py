#add noise and plot
import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

mean = 0
var = 50
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (1728, 3072))

#Directory containing the images. Can replace "jpg" with whatever format your images are in.
path = "testimgs/*jpg"

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

#plot images
        plt.subplot(211)
        plt.title("Input image")
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.subplot(212)
        plt.title("Image with added noise")
        plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
        plt.show()