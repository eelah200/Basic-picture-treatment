import numpy as np, cv2

image = cv2.imread("images/image5.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

background = np.zeros((image.shape[0],image.shape[1]), np.uint8)
background.fill(0)

th1 = 0
th2 = 0
def update_th1(value_alpha):
    global th1
    th1 = value_alpha/100
    update_image()

def update_th2(value_beta):
    global th2
    th2 = value_beta/100
    update_image()

def update_image():
    global th1, th2

    def nonmax_suppression(sobel, direct):
        rows, cols = sobel.shape[:2]
        dst = np.zeros((rows, cols), np.float32)
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                # 행렬 처리를 통해 이웃 화소 가져오기
                values = sobel[i - 1:i + 2, j - 1:j + 2].flatten()
                first = [3, 0, 1, 2]
                id = first[direct[i, j]]
                v1, v2 = values[id], values[8 - id]
                dst[i, j] = sobel[i, j] if (v1 < sobel[i, j] > v2) else 0
        return dst

    def trace(max_sobel, i, j, low):
        h, w = max_sobel.shape
        if (0 <= i < h and 0 <= j < w) == False: return  # 추적 화소 범위 확인
        if pos_ck[i, j] == 0 and max_sobel[i, j] > low:
            pos_ck[i, j] = 255
            canny[i, j] = 255

            trace(max_sobel, i - 1, j - 1, low)  # 추적 함수 재귀 호출 - 8방향 추적
            trace(max_sobel, i, j - 1, low)
            trace(max_sobel, i + 1, j - 1, low)
            trace(max_sobel, i - 1, j, low)
            trace(max_sobel, i + 1, j, low)
            trace(max_sobel, i - 1, j + 1, low)
            trace(max_sobel, i, j + 1, low)
            trace(max_sobel, i + 1, j + 1, low)

    def hysteresis_th(max_sobel, low, high):  # 이력 임계값 수행
        rows, cols = max_sobel.shape[:2]
        for i in range(1, rows - 1):  # 에지 영상 순회
            for j in range(1, cols - 1):
                if max_sobel[i, j] > high:  trace(max_sobel, i, j, low)  # 추적 시작

    pos_ck = np.zeros(image.shape[:2], np.uint8)
    canny = np.zeros(image.shape[:2], np.uint8)

    # 사용자 정의 캐니 에지
    gaus_img = cv2.GaussianBlur(image, (5, 5), 0.3)
    Gx = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 1, 0, 3)  # x방향 마스크
    Gy = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 0, 1, 3)  # y방향 마스크
    sobel = np.fabs(Gx) + np.fabs(Gy)  # 두 행렬 절댓값 덧셈
    # sobel = cv2.magnitude(Gx, Gy)  # 두 행렬 벡터 크기

    directs = cv2.phase(Gx, Gy) / (np.pi / 4)
    directs = directs.astype(int) % 4
    max_sobel = nonmax_suppression(sobel, directs)  # 비최대치 억제
    hysteresis_th(max_sobel, int(th1*100), int(th2*100))  # 이력 임계값

    cv2.imshow("canny_edge", canny)

cv2.imshow("canny_edge", background)
cv2.createTrackbar("th1", "canny_edge", 100, 255, update_th1)
cv2.createTrackbar("th2", "canny_edge", 140, 255, update_th2)

cv2.waitKey(0)