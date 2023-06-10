import cv2

def detect_faces_eyes():
    yuz_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    goz_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    kamera = cv2.VideoCapture(0)

    while True:
        ret, goruntu = kamera.read()

        griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
        yuzler = yuz_cascade.detectMultiScale(griton, 1.3, 5)

        for (x, y, w, h) in yuzler:
            cv2.rectangle(goruntu, (x, y), (x + w, y + h), (0, 0, 255), 3)
            yuz_griton = griton[y:y + h, x:x + w]
            yuz_renkli = goruntu[y:y + h, x:x + w]
            gozler = goz_cascade.detectMultiScale(yuz_griton)

            for (ex, ey, ew, eh) in gozler:
                cv2.rectangle(yuz_renkli, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

        cv2.imshow('Görüntü', goruntu)

        if cv2.waitKey(13) & 0xFF == ord('q'):
            break

    kamera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_faces_eyes()
