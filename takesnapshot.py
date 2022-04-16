import cv2
import time
import random

start_time= time.time()


def takesnapshot():
    number=random.randint(0,100)
    videocaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame= videocaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result= False
    return img_name
    print("snapshot taken")
    videocaptureObject.release()
    cv2.destroyAllWindows()

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=takesnapshot()

//main()