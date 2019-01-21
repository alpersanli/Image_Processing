import cv2

resim=cv2.imread('heartsoul.jpg')
cv2.imshow('orijinal',resim)

cv2.rectangle(resim,(100,200),(500,900),(255,0,0),2)   #sol ust nokta, sag ust nokta, renk, kalinlik
cv2.imshow('dortgen',resim)

cv2.line(resim,(100,200),(500,900),(255,0,0),2)
cv2.imshow('line',resim)

cv2.circle(resim,(100,100),50,(255,0,0),2)  #daire
cv2.imshow('circle',resim)

cv2.putText(resim,'alpppppp',(100,500),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,250),3)  #yazi, sol alttan baslıyor koordinat
cv2.imshow('yazili',resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
