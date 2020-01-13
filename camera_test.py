from TCamera import Camera
import TUtil as utl

# print(cv2.__version__)
# capture = cv2.VideoCapture('big_buck_bunny_720p_10mb.mp4')
# succes, image = capture.read()
# print(succes, image)
# print(cv2.imencode(".jpg", image))

camera=Camera()
camera.bindImageStream("http://192.168.1.22:8081/?action=snapshot")
rslt, img = camera.getFrame(".jpg")
#camera.showImage(img)
print(camera.saveImage(img, "output/" + utl.getTimeStamp() + ".jpg"))
#input("Press Enter to exit...")