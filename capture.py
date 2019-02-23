import cv2


# Захватываем видео поток с камеры
cap = cv2.VideoCapture(0)

print('Для выхода нажмите ESC')

while True:
    ret, frame = cap.read()

    # Добавляем еще один в черно-белом формате
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Main frame', frame)
    cv2.imshow('Gray frame', gray)
    if cv2.waitKey(10) == 0x1b:
        break

cap.release()
cv2.destroyAllWindows()
