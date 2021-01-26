import cv2
from matplotlib import pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

img = cv2.imread("car_4.png")
plt.imshow(img)
plt.show()

bbox, label, conf = cv.detect_common_objects(img)
output_image = draw_bbox(img, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print('Number of cars in the image is ' + str(label.count('car')))