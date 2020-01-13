# import the necessary packages
import numpy as np
import urllib.request
import cv2
 

# download the image, convert it to a NumPy array, and then read
# it into OpenCV format
resp = urllib.request.urlopen("http://192.168.1.22:8081/?action=snapshot")
image = np.asarray(bytearray(resp.read()), dtype=np.uint8)
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

dimensions = image.shape
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)

rslt = cv2.imshow('teste', image)
cv2.waitKey(0);
print(rslt)
cv2.imwrite("./teste.jpg", image) 
cv2.destroyAllWindows()