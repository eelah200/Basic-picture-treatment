import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread("images/image2.jpg", cv2.IMREAD_GRAYSCALE)

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 사각형 중심 좌표 및 크기 설정
        centerPoint = x, y
        startPoint = int(centerPoint[0] - 50), int(centerPoint[1] - 50)
        endPoint = int(centerPoint[0] + 50), int(centerPoint[1] + 50)

        # ROI 추출
        roi = image[startPoint[1]:endPoint[1], startPoint[0]:endPoint[0]]

        # ROI 평활화
        equalized_roi = cv2.equalizeHist(roi)

        # 평활화된 ROI를 원본 이미지에 합치기
        image_with_equalized_roi = np.copy(image)
        image_with_equalized_roi[startPoint[1]:endPoint[1], startPoint[0]:endPoint[0]] = equalized_roi

        # 결과 출력
        cv2.imshow("image", image_with_equalized_roi)

# 초기 화면
cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()


