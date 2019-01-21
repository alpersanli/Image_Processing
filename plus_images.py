import cv2
import numpy as np

img1=cv2.imread('heartsoul.jpg')
img2=cv2.imread('logo.jpg')

satir,sutun,kanal=img2.shape #bilgilerini aldik
roi=img1[0:satir,0:sutun]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)  #resim gri renk oldu
cv2.imshow('img2gray',img2gray)

ret, mask=cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)    #10 dan 255 e kadar filtreleme islemleri siyah haric her yeri beyaz gosterdi
cv2.imshow('mask',mask)

mask_inv=cv2.bitwise_not(mask)  #siyah ile beyaz yer degistirdi
cv2.imshow('mask_inv',mask_inv)

img1_background=cv2.bitwise_and(roi,roi,mask=mask_inv)  #arka planda mask resimi on planda da open cv  ikonu gözuksun
cv2.imshow('img1_background',img1_background)

img2_foregroung=cv2.bitwise_and(img2,img2,mask=mask)    #arka kismini sildi on planinin aldi     sadece
cv2.imshow('img2_foregroung',img2_foregroung)

son_resim=cv2.add(img1_background,img2_foregroung)  #arka plan ve on plan alarak resimleri birlestirdi
img1[0:satir,0:sutun]=son_resim
cv2.imshow('son_resim',son_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
