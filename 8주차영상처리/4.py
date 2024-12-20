import numpy as np, cv2

image = cv2.imread("images/repeat.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

width_num = int(input("가로에 들어갈 개수를 입력하시오. : "))
height_num = int(input("세로에 들어갈 개수를 입력하시오. : "))

background = np.zeros((300, 200, 3), np.uint8)
background.fill(255)

width_resize = int(background.shape[1]/width_num)
height_resize = int(background.shape[0]/height_num)
size = (width_resize, height_resize)

image = cv2.resize(image, size)
image_width = int(image.shape[1])
image_height =int(image.shape[0])

for i in range(height_num):
    for j in range(width_num):
        x = i * image_height
        y = j * image_width
        background[x:x + image_height, y:y + image_width] = image

cv2.imshow("image repeat", background)

cv2.waitKey(0)
cv2.destroyAllWindows()