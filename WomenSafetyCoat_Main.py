from firebase import firebase
import RPi.GPIO as GPIO
import time
import cv2

firebase = firebase.FirebaseApplication('https://women-safety-coat.firebaseio.com/')

a=firebase.get('/WSC_USER',None)

pir=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir,GPIO.IN)
if a['Mode']=='1':
        while True:
                if GPIO.input(pir):
                        GPIO.output(vibrator,True)
                        time.sleep(1)

                        face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                        cap=cv2.VideoCapture(0)
                        a=1
                        while True:
                            ret, frame=cap.read()
                            if a==1:
                                print(ret)
                                a+=1
                            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                            faces=face_cascade.detectMultiScale(gray,1.29,3)
                            for x,y,w,h in faces:
                                roi_gray=gray[y:y+h, x:x+w] #roi is region of interest
                                roi_color = frame[y:y+h, x:x+w]
                                img_item="7.png"
                                cv2.rectangle(frame, (x,y), (x+w,y+h),(115,215,100),3)

                            cv2.imshow('Frame',frame)
                            if cv2.waitKey(20) & 0xff ==ord('q'):
                                break

                        cap.release()
                        cv2.destroyAllWindows()

                else:
                        print('No motion')
                        GPIO.output(vibrator,False)
                        time.sleep(2)
                            
                if cv2.waitKey(20) & 0xff ==ord('q'):
                        break