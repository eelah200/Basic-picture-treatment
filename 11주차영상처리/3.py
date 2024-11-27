import numpy as np, cv2

image = cv2.imread("images/image3.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

B, G, R = cv2.split(image)

red_channel = cv2.merge([B * 0 , G * 0 , R])
blue_channel = cv2.merge([B , G * 0 , R * 0])
green_channel = cv2.merge([B * 0 , G, R * 0])

cv2.imshow("Red_channel", red_channel)
cv2.imshow("Blue_channel", blue_channel)
cv2.imshow("Green_channel", green_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()