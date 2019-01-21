import cv2

kamera=cv2.VideoCapture(0)   #(0)pc kamerası,(1)usb kamera,('smile')yukledıgın video

kamera.set(cv2.CAP_PROP_FRAME_WIDTH,250)    #kamera boyutlari
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,250)

while True:     #while dogru oldugu muddetçe
    ret, goruntu=kamera.read()  #return demek

    #########kamera set boyle de ayarlanabilir 2.yol
    #ret=kamera.set(3,320)   #3.bilgi width
    #ret=kamera.set(4,240)   #4.bilgi height
    griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)  #gri ton
    cv2.imshow('griton', griton)

    farklirenk = cv2.cvtColor(goruntu, cv2.COLOR_BGR2LUV)
    cv2.imshow('farklirenk', farklirenk)

    cv2.imshow('goruntu',goruntu)

    if cv2.waitKey(25) & 0xFF==ord('q'):     #q ya basıldıgında kapanacak 25 hız
        break

kamera.release()    #bırak kapat
cv2.destroyAllWindows()
