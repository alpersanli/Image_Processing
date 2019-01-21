import cv2
import numpy as np

mypicture=cv2.imread('heartsoul.jpg')

#print(str(mypicture.item(100,100,1)))  #100e100 pikselinin yesil değerini verir. 0mavı 1yesil 2kirmizi
#mypicture.itemset((100,100,2),255)  #255 kırmızı nokta koydu

#print(str(mypicture.shape))     #yukseklik genislik ve kanal sayısı. yukarida 0 yazarsan 3 yok olur.bu sayede renkli renksiz anlariz
#print(str(len(mypicture.shape)))    #siyah beyazsa 2, renkliyse 3 yazar

#print("renkli resim :"+str(mypicture.size))      #toplam piksel sayisini verir
#mypicture=cv2.imread('heartsoul.jpg',0)     #renksiz
#print('renksiz resim  :'+str(mypicture.size))      #renksiz piksel 1/3 olur cunku mavi yesil kimizi değil tek layer var

#print(mypicture.dtype)      #resimlerin toplanmasi icin data tiplerinin ayni olmasi lazim
#ROI=mypicture[100:500,200:400]   #bolum kestik y,x aralıkları
#cv2.imshow('roi nin goruntusu',ROI)     #kesilen bolumu gosterdik
#mypicture[100:500,600:800]= ROI   #resim ustune resim yapistirdi ama dikkat et aralık farklari bir once kestiginle ayni olmali

#mypicture[:,:,2]=0  #mavi bilesenini 0 yaptik



cv2.imshow('nice picture',mypicture)
cv2.waitKey(0)
cv2.destroyAllWindows()
