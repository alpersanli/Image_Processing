import cv2
import numpy as np

def metin_yaz():
    img=np.zeros((640,720,3),np.uint8)  #alanı olusturduk,3 renk oldugunu belirttik
    img.fill(255)

    fontscale=1.0
    color=(0,0,255)

    fontface=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,"FONT_HERSHEY_COMPLEX",(25,40),fontface,fontscale,color)

    fontface=cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img,"FONT_HERSHEY_COMPLEX_SMALL",(25,60),fontface,fontscale,color)

#bir suru farkli yazi tipi var

    cv2.namedWindow('text ornekler')
    cv2.imshow('text ornekler',img)
    cv2.imwrite('text_ornekler.jpg',img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    metin_yaz()

if __name__=="__main__":
    main()
