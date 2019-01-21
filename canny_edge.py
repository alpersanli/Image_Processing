import cv2
import numpy as np

kamera=cv2.VideoCapture(0)   #(0)pc kamerası,(1)usb kamera,('smile')yukledıgın video

while True:     #while dogru oldugu muddetçe
    ret, frame=kamera.read()  #return demek

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk_mavi=np.array([100,60,60])
    ust_mavi=np.array([140,255,255])

    kenarlar=cv2.Canny(frame,100,150)
    kenarlar2 = cv2.Canny(frame, 50, 50)
    kenarlar3 = cv2.Canny(frame, 0, 0)

    mask=cv2.inRange(hsv,dusuk_mavi,ust_mavi)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('canny_kenar',kenarlar)
    cv2.imshow('canny_kenar2', kenarlar2)
    cv2.imshow('canny_kenar3', kenarlar3)

    if cv2.waitKey(25) & 0xFF==ord('q'):     #q ya basıldıgında kapanacak 25 saniyede aldıgı goruntu
        break
kamera.release()    #bırak kapat
cv2.destroyAllWindows()

