# https://github.com/aladdinpersson/Machine-Learning-Collection/blob/master/ML/Pytorch/Basics/albumentations_tutorial/classification.py

from albumentations.augmentations.crops.transforms import RandomCrop
from albumentations.augmentations.geometric.rotate import Rotate
from albumentations.augmentations.transforms import HorizontalFlip, RGBShift
import cv2
import albumentations as A
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

image = Image.open('Albumenations\images\elon.jpeg')
# image.show()

transform = A.Compose([
    A.Resize(width = 224, height = 224),
    A.RandomCrop(width = 224, height = 224),
    A.Rotate(limit = 40, p = 0.9, border_mode = cv2.BORDER_CONSTANT), 
    A.HorizontalFlip(p = 0.5),
    A.VerticalFlip(p = 0.1),
    A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.9),
        A.OneOf([
            A.Blur(blur_limit=3, p=0.5),
            A.ColorJitter(p=0.5),
        ], p=1.0),])

image_list = [image]
image = np.array(image)

for i in range(5):
    augmentations = transform(image=image)
    augmented_img = augmentations['image']
    image_list.append(augmented_img)

print(image_list)

for i in image_list:
    plt.imshow(i, interpolation='nearest')
    plt.show()


# https://github.com/aladdinpersson/Machine-Learning-Collection/blob/master/ML/Pytorch/Basics/albumentations_tutorial/classification.py