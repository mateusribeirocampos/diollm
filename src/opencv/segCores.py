import cv2  
from matplotlib import pyplot as plt
import numpy as np  
import requests 

"""url = 'https://assets.architecturaldigest.in/photos/60083e9908ae763b9ae8540f/16:9/w_1600,c_limit/artificial-grass-turf-pros-cons-pexels-free-nature-stock-7174-1366x768.jpg' 
r = requests.get(url, allow_redirects=True)
with open('lena.jpg', 'wb') as f: 
    f.write(r.content)"""

img = cv2.imread('/Users/mateusribeirodecampos/myProjects/diollm/grass.jpg') 
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.axis('off')
plt.show()

rgb_green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(rgb_green, cv2.COLOR_RGB2HSV)[0,0,:]
print(hsv_green)

"""thresholding_shematics = cv2.cvtColor(cv2.imread('hsv_th.png'), cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.imshow(thresholding_shematics)
plt.title('Thresholding Semantics')
plt.axis('off')
plt.savefig('thresholding_semantics_output.png', bbox_inches='tight')
plt.clf()"""

hsv_im = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

lower_th = hsv_green - np.array([70,202,202])
upper_th = hsv_green + np.array([30,0,0])

mask = cv2.inRange(img, lower_th, upper_th)

plt.figure(figsize=(10,10))
plt.imshow(mask)
plt.show()

rgb_res = cv2.bitwise_and(img, img, mask=mask)

plt.figure(figsize=(10,10))
plt.imshow(rgb_res)
plt.show()