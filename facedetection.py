import cv2

faceCascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

print('Для выхода нажмите ESC')

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('Main frame',img)

    if cv2.waitKey(10) == 0x1b:
        break

cap.release()
cv2.destroyAllWindows()