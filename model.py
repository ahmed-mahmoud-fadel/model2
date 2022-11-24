import cv2
# import webbrowser

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalcatface.xml')
pro_cascade = cv2.CascadeClassifier(r'haarcascade_profileface.xml')
cap = cv2.VideoCapture(0)

while 1:

    (ret, img) = cap.read()
    img=cv2.flip(img,1,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    pros = pro_cascade.detectMultiScale(img,1.3,5)
    if len (pros) == 0 :
        pros = pro_cascade.detectMultiScale(cv2.flip(img,1,1),1.3,5)
        for n in pros:
            n[0] = 640 - n[0] - n[3]
            
    if ((len(faces)==0)&(len(pros)>0)):
        for (x,y,w,h) in pros:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            # url = 'http://smarter.epizy.com/cheater.php'
            # webbrowser.open(url, new=0)
            cv2.waitKey(100)
    elif(len(faces)>0):
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.waitKey(100)
    cv2.imshow('img',img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()