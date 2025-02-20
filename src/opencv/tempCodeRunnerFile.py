rgb_green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(rgb_green, cv2.COLOR_RGB2HSV)[0,0,:]
print(hsv_green)