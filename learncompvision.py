import cv2
a = cv2.imread("linus.jpg", 1)   #1 - coloured image
print(a)
print(a.shape)
b = cv2.imread("linus.jpg", 0)
print(b)
print(type(b))
print(b.shape)

a = cv2.imread("linus.jpg", 1)
new = cv2.resize(a, (600, 500))        # Width X Height
new = cv2.resize(a, (int(a.shape[1]/3), int(a.shape[0]/4)))               # Width X Height
cv2.imshow("Linus", new)
cv2.waitKey(0)
# cv2.waitKey(1000)
cv2.destroyAllWindows()

# FACE DETECTION + EYES DETECTION
# create a cascade classifier object
face_cascade = cv2.CascadeClassifier("C:\\Users\\Aakash Garg\\PycharmProjects\\Learn Python\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\Aakash Garg\\PycharmProjects\\Learn Python\\haarcascade_eye.xml")
img = cv2.imread("C:\\Users\\Aakash Garg\\PycharmProjects\\Learn Python\\linus.jpg")
print("Original Dimensions: ", img.shape)
resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)), interpolation=cv2.INTER_AREA)
print("Resized Dimensions: ", resized.shape)
# cv2.imshow("Linus", resized)
# cv2.waitKey(0)
gray_img = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Linus", gray_img)
# cv2.waitKey(0)
# search the co-ordinates of the image - face_rectangle
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=2)
print(type(faces))
print(faces)

if faces is ():
    print("No faces found")
for (x, y, w, h) in faces:
    cv2.rectangle(resized, (x, y), (x + w, y + h), (127, 0, 255), 2)
    cv2.imshow('Face Detection', resized)
    cv2.waitKey(1000)
    roi_gray = gray_img[y:y+h, x:x+w]
    roi_color = resized[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 255), 2)
        cv2.imshow('Eyes', resized)
        cv2.waitKey(1000)
cv2.destroyAllWindows()

# VIDEO CAPTURE
import time
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
check, frame = video.read()
print(check)
# print(frame)
time.sleep(3)
cv2.imshow('Capturing', frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()

# CAPTURE VIDEO
video = cv2.VideoCapture(0)
a = 1
while True:
    a = a+1
    check, frame = video.read()
    # print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing', gray)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
print(a)
video.release()
cv2.destroyAllWindows()

# USE CASE
# video = cv2.VideoCapture(0)
# a = 1
# first_frame = None
# while True:
#     a = a + 1
#     check, frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, (21, 21), 0)
#     if first_frame is None:
#         first_frame = gray
#         continue
#     delta_frame = cv2.absdiff(first_frame, gray)
#     thres_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
#     thres_delta = cv2.dilate(thres_delta, None, iterations=0)
#     (_,cnts,_) = cv2.findContours(thres_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for contours in cnts:
#         if cv2.contourArea(contours)<1000:
#             continue
#         (x, y, w, h) = cv2.boundingRect(contours)
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0) ,3)
#         key = cv2.waitKey(1)
#         if key == ord("q"):
#             break
#
# cv2.imshow('frame', frame)
# cv2.imshow('Capturing', gray)
# cv2.imshow('delta', delta_frame)
# cv2.imshow('thres', thres_delta)
# video.release()
# cv2.destroyAllWindows()

# PRACTICE
class_face = cv2.CascadeClassifier("C:\\Users\\Aakash Garg\\PycharmProjects\\Learn Python\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\Aakash Garg\\PycharmProjects\\Learn Python\\haarcascade_eye.xml")
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
a = 1
while True:
    a += 1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = class_face.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=2)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow('Capturing', frame)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 255), 2)
            cv2.imshow('Eyes', frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    # gauss = cv2.GaussianBlur(gray, (21,21), 0)
    # cv2.imshow('Capturing', gray)
    # cv2.imshow('Capturing', gauss)
    # key = cv2.waitKey(1)
    # if key == ord("q"):
    #     break
video.release()
cv2.destroyAllWindows()