from datetime import datetime
import time
import RPi.GPIO as GPIO
import filesUpload as fileUp
import Startup4 as st3
import jtalk as j

#interval
INTERVAL = 1
# sleep time
SLEEPTIME = 5 
# use GPIO
GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN,GPIO.IN)

if __name__ == '__main__':
    try:
        print('cancel processing: ctrl + c')
        cnt = 1
        while True:
            # detect sensor
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                print(datetime.now().strftime("%Y%m%d %H:%M:%S") + ":"+str("{0:05d}".format(cnt)+"time detection"))
                cnt = cnt + 1
                j.talk_greeting()
                # start image capture : Startup3.py->imageCapture()
                st3.imageCapture()
                time.sleep(SLEEPTIME)
            else:
                print(GPIO.input(GPIO_PIN))
                time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Finishing Process")
    finally:
        GPIO.cleanup()
        print("GPIO Complete clean up ")
        
                
            

