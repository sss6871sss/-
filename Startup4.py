# coding: utf-8
import picamera
import picamera.array
import cv2
import filesUpload as fileUp
import os
import datetime
import jtalk as j

def imageCapture():
    GlobalCounter = 0
    face_cascade_file = "haarcascade_frontalface_default.xml"
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('frame',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as stream:
            camera.resolution = (320, 240)
            while True:
                # stream.arrayにRGBの順で映像データを格納
                camera.capture(stream, 'bgr', use_video_port=True)
                
                # グレースケールに変換
                gray = cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)
                
                # カスケードファイルを利用して顔の位置を見つける
                f_cascade = cv2.CascadeClassifier(face_cascade_file)
                face_list = f_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
                
                for (x, y, w, h) in face_list:
                    print("face_position:",x, y, w, h)
                    # uploadSlack
                    ret = uploadSlack(stream.array,gray,x,y,w,h)
                    if ret == True:
                        cv2.destroyAllWindows()
                        j.talk_weather()
                        return
                    
                # system.arrayをウィンドウに表示
                cv2.imshow('frame', stream.array)
                    
                # "q"でウィンドウを閉じる
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

                # streamをリセット
                stream.seek(0)
                stream.truncate()
            cv2.destroyAllWindows()
            return

def saveImageFile(img):
    imgDir = "./img/"
    date_dir = '{0:%Y%m%d}'.format(datetime.date.today())
    # exist img dir
    if not os.path.exists(imgDir):
        # create img dir
        os.mkdir(imgDir)    

    # exist date dir
    if not os.path.exists(imgDir + date_dir):
        # create date dir
        os.mkdir(imgDir + date_dir)

    path = imgDir + date_dir + '/'
    filename = date_dir + '-' + '{0:%H%M%S}'.format(datetime.datetime.today()) + '.png'
    cv2.imwrite(path + filename,img)

    index = len(os.listdir(path))

    msg = str(datetime.date.today()) + " " + str(index) + "人目のお客様です。" 

    return path+filename,msg,filename

        
def uploadSlack(img,gray,x,y,w,h):
    eye_cascade_file = "haarcascade_eye.xml"
    e_cascade = cv2.CascadeClassifier(eye_cascade_file)
    color = (255, 255, 255)
    pen_w = 2
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = e_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        filename,msg,title = saveImageFile(img)
        # send Slack
        fileUp.sendSlack(filename,msg,title)
        return True

    return False


