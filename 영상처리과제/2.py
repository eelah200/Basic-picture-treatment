import numpy as np, cv2

image = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if image is None or logo is None: raise Exception("영상파일 읽기 오류")

width_num = int(input("가로에 들어갈 개수를 입력하시오. : "))
height_num = int(input("세로에 들어갈 개수를 입력하시오. : "))

width_resize = int(image.shape[1]/width_num)
height_resize = int(image.shape[0]/height_num)
size = (width_resize, height_resize)
logo = cv2.resize(logo, size)

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

for i in range(height_num):
    for j in range(width_num):
        x = j * width_resize
        y = i * height_resize
        roi = image[y:y + height_resize, x:x + width_resize]

        foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
        background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)
        dst = cv2.add(background, foreground)
        image[y:y+height_resize, x:x+width_resize] = dst

cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
