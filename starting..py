import os
from PIL import Image
import cv2
import skimage as sk
from skimage import io as sk_io
import matplotlib.pyplot as plt
from matplotlib import image as mp_image


images = []

src_folder = "C:/Users/merts/Documents/GitHub/vision_course/Images_1"

pil_image = Image.open(os.path.join(src_folder,"009834.jpg"))
images.append(pil_image)
sk_image = sk_io.imread(os.path.join(src_folder,"009432.jpg"))
images.append(sk_image)
cv_image = cv2.imread(os.path.join(src_folder,"009597.jpg"))
images.append(cv_image)

fig = plt.figure(figsize=(12,12))

image_count = 0
total_images = len(images)

for i in range(total_images):
    a = fig.add_subplot(1, total_images, i+1)
    image_plot = plt.imshow(images[i])
    a.set_title("Image" + str(i+1))

plt.show()