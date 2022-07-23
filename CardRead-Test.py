import cv2
import numpy as np
import dlib
import easyocr

detector = dlib.fhog_object_detector('./train03.svm')
predictor = dlib.shape_predictor('./shapePredict3.dat')

frame = cv2.imread(
    './imgForTest/290681496_1361817587658553_8747890748007727090_n.jpg')

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

rects = detector(gray, 0)

for rect in rects:
    (x, y, w, h) = (rect.left(), rect.top(),
                    (rect.right() - rect.left()), rect.bottom() - rect.top())

    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    shape = predictor(gray, rect)
    for i in range(len(shape.parts())):
        cv2.circle(frame, (shape.part(i).x, shape.part(i).y),
                   3, (255, 255, 255), -1)
        pts1 = np.float32([[shape.part(0).x, shape.part(0).y], [shape.part(3).x, shape.part(
            3).y], [shape.part(1).x, shape.part(1).y], [shape.part(2).x, shape.part(2).y]])




        pts2 = np.float32([[0, 0], [600, 0], [0, 400], [600, 400]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(gray, M, (600, 400))

# img_d[90:230, 150:455] => name, student_id, faculty
# name => [125:155, 150:455]

img_d = dst.copy()
crop_name = img_d[125:155, 150:455]
crop_student_id = img_d[155:185, 245:455]
crop_faculty = img_d[180:215, 150:455]

reader = easyocr.Reader(['en', 'th'], gpu=True)
text_name = reader.readtext(crop_name)
text_student_id = reader.readtext(crop_student_id)
text_faculty = reader.readtext(crop_faculty)
# print(result)
cv2.imshow('detect frame', frame)
# cv2.imshow('warp frame', dst)
cv2.imshow('crop warp image', img_d)
cv2.imshow('crop name', crop_name)
cv2.imshow('crop student_id', crop_student_id)
cv2.imshow('crop faculty', crop_faculty)
# old card = 5 7 10, new card = 3 4 5
name = text_name[0][1].strip()
student_id = text_student_id[0][1]
faculty = text_faculty[0][1].strip()[3:]
# name = text_name[1].replace('.','').strip()
# student_id = text_student_id[1].strip().split(" ")[1]
# faculty = text_faculty[1]
print(text_name, text_student_id, text_faculty)
# print(text_name)
print(student_id, name, faculty)
# print(name)

key = cv2.waitKey()
if key == ord('q'):
    exit()

cv2.destroyAllWindows()

