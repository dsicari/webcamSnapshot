import cv2
 
capture = cv2.VideoCapture("http://192.168.1.22:8081/?action=snapshot")

ret, frame = capture.read()

cv2.imshow('video', frame)
input("Press Enter to exit...")
 
capture.release()
cv2.destroyAllWindows()