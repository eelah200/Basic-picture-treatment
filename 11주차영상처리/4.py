import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread("images/image4.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

# ROI 내 히스토그램 계산
def draw_histo(hist, shape=(200,256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)

    return cv2.flip(hist_img, 0)


initial_image = np.copy(image)
startPoint = None
endPoint = None
def onMouse(event, x, y, flags, param):
    global startPoint, endPoint, image

    if event == cv2.EVENT_LBUTTONDOWN:
        if startPoint == None:
            startPoint = (x, y)
        elif endPoint == None:
            endPoint = (x, y)
            print(startPoint, endPoint)
            # ROI 추출, 영역 지정
            roi = image[startPoint[1]:endPoint[1], startPoint[0]:endPoint[0]]
            # ROI 영역에 사각형 그리기
            cv2.rectangle(image, startPoint, endPoint, 0, 1, cv2.LINE_4)
            # 히스토그램 그래프 적용
            hist = cv2.calcHist([roi], [0], None, [32], [0, 256])
            hist_img = draw_histo(hist)
            # 결과 출력
            cv2.imshow("result", image)
            cv2.imshow("hist_img", hist_img)
        else:  # 두 점이 모두 지정되었으면 초기화
            image = np.copy(initial_image)
            startPoint = (x,y)
            endPoint = None

# 초기 화면
cv2.imshow("result", image)
cv2.setMouseCallback("result", onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()