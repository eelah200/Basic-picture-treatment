import numpy as np
import cv2

def scaling(img, size):  # 크기 변경 함수
    dst = np.zeros((*size[::-1], img.shape[2]), img.dtype)  # 채널까지 고려한 목적지 배열 생성
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for y in range(img.shape[0]):  # 입력 영상 순회 - 순방향 사상
        for x in range(img.shape[1]):
            i, j = int(y * ratioY), int(x * ratioX)  # 목적 영상의 y, x 좌표
            dst[i, j] = img[y, x]  # RGB 픽셀 값 복사
    return dst

def onMouse(event, x, y, flags, param):
    global initial_image
    if event == cv2.EVENT_LBUTTONDOWN:
        initial_image = (int(initial_image[0]*1.1), int(initial_image[1]*1.1))

    elif event == cv2.EVENT_RBUTTONDOWN:
        initial_image = (int(initial_image[0] * 0.9), int(initial_image[1] * 0.9))

    adjust = scaling(image, initial_image)
    cv2.imshow("adjust", adjust)

# 입력 이미지 읽기
image = cv2.imread('images/image1.jpg')
if image is None: raise Exception("영상 파일을 읽는 중 에러가 발생했습니다")

initial_image = image.shape[1], image.shape[0]




cv2.imshow("adjust", image)
cv2.setMouseCallback("adjust", onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
