from random import choice

import numpy as np
import cv2
import math

# 창 화면 구성
image = np.zeros((300,400), np.uint8)
image.fill(255)
black = (0, 0, 0)

pt1, pt2 = (200, 0), (200, 300)
pt3, pt4 = (0, 150), (400, 150)

cv2.line(image, pt1, pt2, black)
cv2.line(image, pt3, pt4, black)

# 국기 기본화면 구성
japan = np.zeros((400,400,3), np.uint8)
japan.fill(255)

czech = np.zeros((400,400,3), np.uint8)

algeria = np.zeros((400,400,3), np.uint8)

korea = np.zeros((400,600, 3), np.uint8)
korea.fill(255)

# 일본그리기
# 유클리드 거리를 이용한 원그리기
center_x = 200
center_y = 200
radius = 50
circle = []
for x in range(center_x - radius, center_x + radius):
    for y in range(center_y - radius, center_y + radius):
        if math.sqrt((x - center_x)**2 + (y - center_y)**2) <= radius:
            japan[y, x] = 0
            circle.append((y,x))

title = 'japan'
def track_blue(value):
    global japan, title
    for (y, x) in circle:
        japan[y,x,0] = value
    cv2.imshow(title, japan)

def track_red(value):
    global japan, title
    for (y, x) in circle:
        japan[y,x,2] = value
    cv2.imshow(title, japan)

def track_green(value):
    global japan, title
    for (y, x) in circle:
        japan[y,x,1] = value
    cv2.imshow(title, japan)

# 체코 그림 그리기
# 직선의 기울기를 이용한 체코 그리기
start_width = 50
start_height = 50
width = 300
height = 200
white = (255, 255, 255)
red = (0, 0, 255)
blue = (255, 0, 0)

for y in range(start_height, start_height + height):
    for x in range(start_width, start_width + width):
        if y <= start_height + height/2:
            czech[y, x] = white

for y in range(start_height, start_height + height):
    for x in range(start_width, start_width + width):
        if y >= start_height + height/2:
            czech[y, x] = red

for y in range(start_height, start_height + int(height/2)):
    for x in range(start_width, width):
        gradient_upper = (start_height - (start_height+height/2)) / (start_width - (start_width+width/2))
        distance_upper = gradient_upper * (x - start_width) + start_height
        if y >= distance_upper:
            czech[y, x] = blue

for y in range(start_height+int(height/2), start_height + height):
    for x in range(start_width, width):
        gradient_down = (start_height - (start_height+height/2)) / (start_width - (start_width+width/2))
        distance_down = (gradient_down * (start_width - x) + (start_height + height))
        if y <= distance_down:
            czech[y, x] = blue

# 알제리 그리기
start_width = 50
start_height = 50
width = 300
height = 200
white = (255, 255, 255)
red = (0, 0, 255)
green = (0, 255, 0)
algeria_center = (int(start_width+(width/2)), int(start_height+(height/2)))
algeria_radius = 50

# 그믐달 그리기
for y in range(start_height, start_height + height):
    for x in range(start_width, start_width + width):
        if x <= start_width + width/2:
            algeria[y, x] = green

for y in range(start_height, start_height + height):
    for x in range(start_width, start_width + width):
        if x >= start_width + width/2:
            algeria[y, x] = white

decre_radius = 9
smal_center = (algeria_center[0] + decre_radius, algeria_center[1])
cv2.circle(algeria, algeria_center, algeria_radius, red, -1)
cv2.circle(algeria, smal_center, algeria_radius-decre_radius, white, -1)

#별 그리기
center_x, center_y = 210, 150  # 오각형 중심
r_outer = 10  # 큰 반지름
r_inner = 5   # 작은 반지름

points = []
# 외부 꼭짓점 좌표 계산
for i in range(5):
    angle = i * (360 / 5) * (np.pi / 180)
    x = int(center_x + r_outer * np.cos(angle))
    y = int(center_y + r_outer * np.sin(angle))
    points.append((x, y))

# 내부 꼭짓점 좌표 계산
for i in range(5):
    angle = i * (360 / 5) * (np.pi / 180) + (360 / 10) * (np.pi / 180)
    x = int(center_x + r_inner * np.cos(angle))
    y = int(center_y + r_inner * np.sin(angle))
    points.append((x, y))

# 내부, 외부 꼭짓점 교차 배열
points = np.array(points, np.int32)
points = points.reshape((-1, 1, 2))

out_point = points[:5]
in_point = points[5:]

star_points = []
for i in range(5):
    star_points.append(out_point[i])
    star_points.append(in_point[i])

star_points = np.array(star_points, np.int32)


# 태극기 그리기
black = (0,0,0)
red = (0,0,255)
blue = (255,0,0)

center_x, center_y = 300, 200  # 중심점
radius = 100

geon = [
    np.array([(center_x, center_y), (center_x+100, center_y), (center_x+100, center_y+20), (center_x, center_y+20)]),  # 첫 번째 막대 (위쪽)
    np.array([(center_x, center_y+40), (center_x+100, center_y+40), (center_x+100, center_y+60), (center_x, center_y+60)]),  # 두 번째 막대 (중간)
    np.array([(center_x, center_y+80), (center_x+100, center_y+80), (center_x+100, center_y+100), (center_x, center_y+100)])  # 세 번째 막대 (아래쪽)
]
geon_move = np.array([-220,-160])
geon = [geon[0] + geon_move, geon[1] + geon_move, geon[2] + geon_move]

gon = [
    np.array([(center_x, center_y), (center_x+40, center_y), (center_x+40, center_y+20), (center_x, center_y+20)]),
    np.array([(center_x+60, center_y), (center_x+100, center_y), (center_x+100, center_y+20), (center_x+60, center_y+20)]),

    np.array([(center_x, center_y+40), (center_x+40, center_y+40), (center_x+40, center_y+60), (center_x, center_y+60)]),
    np.array([(center_x+60, center_y+40), (center_x+100, center_y+40), (center_x+100, center_y+60), (center_x+60, center_y+60)]),

    np.array([(center_x, center_y+80), (center_x+40, center_y+80), (center_x+40, center_y+100), (center_x, center_y+100)]),
    np.array([(center_x+60, center_y+80), (center_x+100, center_y+80), (center_x+100, center_y+100), (center_x+60, center_y+100)])
]
gon_move = np.array([120,50])
gon = [gon[0] + gon_move, gon[1] + gon_move, gon[2] + gon_move, gon[3] + gon_move, gon[4] + gon_move, gon[5] + gon_move]

gam = [
    np.array([(center_x, center_y), (center_x+40, center_y), (center_x+40, center_y+20), (center_x, center_y+20)]),
    np.array([(center_x+60, center_y), (center_x+100, center_y), (center_x+100, center_y+20), (center_x+60, center_y+20)]),

    np.array([(center_x, center_y+40), (center_x+100, center_y+40), (center_x+100, center_y+60), (center_x, center_y+60)]),

    np.array([(center_x, center_y+80), (center_x+40, center_y+80), (center_x+40, center_y+100), (center_x, center_y+100)]),
    np.array([(center_x+60, center_y+80), (center_x+100, center_y+80), (center_x+100, center_y+100), (center_x+60, center_y+100)])
]
gam_move = np.array([120,-160])
gam = [gam[0] + gam_move, gam[1] + gam_move, gam[2] + gam_move, gam[3] + gam_move, gam[4] + gam_move]

ri = [
    np.array([(center_x, center_y), (center_x+100, center_y), (center_x+100, center_y+20), (center_x, center_y+20)]),

    np.array([(center_x, center_y+40), (center_x+40, center_y+40), (center_x+40, center_y+60), (center_x, center_y+60)]),
    np.array([(center_x+60, center_y+40), (center_x+100, center_y+40), (center_x+100, center_y+60), (center_x+60, center_y+60)]),

    np.array([(center_x, center_y+80), (center_x+100, center_y+80), (center_x+100, center_y+100), (center_x, center_y+100)])
]
ri_move = np.array([-220,50])
ri = [ri[0] + ri_move, ri[1] + ri_move, ri[2] + ri_move, ri[3] + ri_move]

geon_rotation = cv2.getRotationMatrix2D((130, 80), 45, 1)  # 회전 행렬
geon_0_rotated = cv2.transform(geon[0].reshape(-1, 1, 2), geon_rotation)
geon_1_rotated = cv2.transform(geon[1].reshape(-1, 1, 2), geon_rotation)
geon_2_rotated = cv2.transform(geon[2].reshape(-1, 1, 2), geon_rotation)
geon_rotate = np.array([geon_0_rotated, geon_1_rotated, geon_2_rotated])

gon_rotation = cv2.getRotationMatrix2D((470, 300), 45, 1)  # 회전 행렬
gon_0_rotated = cv2.transform(gon[0].reshape(-1, 1, 2), gon_rotation)
gon_1_rotated = cv2.transform(gon[1].reshape(-1, 1, 2), gon_rotation)
gon_2_rotated = cv2.transform(gon[2].reshape(-1, 1, 2), gon_rotation)
gon_3_rotated = cv2.transform(gon[3].reshape(-1, 1, 2), gon_rotation)
gon_4_rotated = cv2.transform(gon[4].reshape(-1, 1, 2), gon_rotation)
gon_5_rotated = cv2.transform(gon[5].reshape(-1, 1, 2), gon_rotation)
gon_rotate = np.array([gon_0_rotated, gon_1_rotated, gon_2_rotated, gon_3_rotated, gon_4_rotated, gon_5_rotated])

gam_rotation = cv2.getRotationMatrix2D((480, 80), -45, 1)  # 회전 행렬
gam_0_rotated = cv2.transform(gam[0].reshape(-1, 1, 2), gam_rotation)
gam_1_rotated = cv2.transform(gam[1].reshape(-1, 1, 2), gam_rotation)
gam_2_rotated = cv2.transform(gam[2].reshape(-1, 1, 2), gam_rotation)
gam_3_rotated = cv2.transform(gam[3].reshape(-1, 1, 2), gam_rotation)
gam_4_rotated = cv2.transform(gam[4].reshape(-1, 1, 2), gam_rotation)
gam_rotate = np.array([gam_0_rotated, gam_1_rotated, gam_2_rotated, gam_3_rotated, gam_4_rotated])

ri_rotation = cv2.getRotationMatrix2D((120, 300), -45, 1)  # 회전 행렬
ri_0_rotated = cv2.transform(ri[0].reshape(-1, 1, 2), ri_rotation)
ri_1_rotated = cv2.transform(ri[1].reshape(-1, 1, 2), ri_rotation)
ri_2_rotated = cv2.transform(ri[2].reshape(-1, 1, 2), ri_rotation)
ri_3_rotated = cv2.transform(ri[3].reshape(-1, 1, 2), ri_rotation)
ri_rotate = np.array([ri_0_rotated, ri_1_rotated, ri_2_rotated, ri_3_rotated])


# 마우스 이벤트
def choiceSector(choice, bg_x, bg_y, flags, param):
    if choice == cv2.EVENT_LBUTTONDOWN:
        print("좌표위치: ", bg_x, bg_y)
        if (bg_x < 200) and (bg_y < 150):
            cv2.imshow(title, japan)
            cv2.createTrackbar("blue", title, 0, 255, track_blue)
            cv2.createTrackbar("green", title, 0, 255, track_green)
            cv2.createTrackbar("red", title, 255, 255, track_red)
        if (bg_x > 200) and (bg_y < 150):
            cv2.imshow("Czech", czech)
        if (bg_x < 200) and (bg_y > 150):
            cv2.fillPoly(algeria, [star_points], red)
            cv2.imshow("Algeria", algeria)
        if (bg_x > 200) and (bg_y > 150):
            cv2.ellipse(korea, (center_x, center_y), (radius, radius), 180, 180, 360, blue, -1)
            cv2.ellipse(korea, (center_x, center_y), (radius, radius), 0, 180, 360, red, -1)
            cv2.circle(korea, (center_x - radius // 2, center_y), radius // 2, red, -1)
            cv2.circle(korea, (center_x + radius // 2, center_y), radius // 2, blue, -1)
            cv2.fillPoly(korea, geon_rotate, black)
            cv2.fillPoly(korea, gon_rotate, black)
            cv2.fillPoly(korea, gam_rotate, black)
            cv2.fillPoly(korea, ri_rotate, black)
            cv2.imshow("Korea", korea)

cv2.putText(image, "Japan", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, black)
cv2.putText(image, "Czech", (250, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, black)
cv2.putText(image, "Algeria", (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, black)
cv2.putText(image, "Korea", (250, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, black)

cv2.imshow("choice", image)
cv2.setMouseCallback("choice", choiceSector)

cv2.waitKey(0)
cv2.destroyAllWindows()
