import numpy as np
import cv2

image = np.zeros((700,900), np.uint8)
image.fill(0)

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)

alpha = 0
beta = 0

def update_alpha(value_alpha):
    global alpha
    alpha = value_alpha/100
    update_image()

def update_beta(value_beta):
    global beta
    beta = value_beta/100
    update_image()

def update_image():
    global alpha, beta
    add_img = cv2.addWeighted(image1, alpha, image2, beta, 0)
    dst = cv2.hconcat([image1, add_img, image2])
    cv2.imshow("dst", dst)


cv2.imshow("dst", image)
cv2.createTrackbar("image1", "dst", 60, 100, update_alpha)
cv2.createTrackbar("image2", "dst", 70, 100, update_beta)

cv2.waitKey(0)
cv2.destroyAllWindows()
