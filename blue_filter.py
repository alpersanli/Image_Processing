import cv2
import numpy as np

kamera=cv2.VideoCapture(0)   #(0)pc kamerası,(1)usb kamera,('smile')yukledıgın video

while True:     #while dogru oldugu muddetçe
    ret, frame=kamera.read()  #return demek

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #dusuk_mavi=np.array([100,60,60])       #mavi icin
    #ust_mavi=np.array([140,255,255])

    dusuk_sari = np.array([5, 100, 100])  # sari icin
    ust_sari = np.array([40, 255, 256])

    dusuk_beyaz=np.array([0,0,140])     #beyaz icin
    ust_beyaz=np.array([256,60,256])

    mask=cv2.inRange(hsv,dusuk_sari,ust_sari)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    

    cv2.imshow('orjinal', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('son_resim',son_resim)

    if cv2.waitKey(25) & 0xFF==ord('q'):     #q ya basıldıgında kapanacak 25 saniyede aldıgı goruntu
        break

kamera.release()    #bırak kapat
cv2.destroyAllWindows()
