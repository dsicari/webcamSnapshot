# Processamento video e imagem
import cv2
# Para abrir imagem de URL
import numpy as np
import urllib.request as urllib

class Camera:
    
    # Status
    STATUS_OK = 0
    # Errors
    SOURCE_NOT_FOUND = -1
    FILE_EXTENSION_NOT_AVAILABLE = -2
    NO_STREAM_BINDED = -3
    FAIL_TO_CONVERT = -4
    IMAGE_NOT_FOUND = -5
    FAIL_TO_SAVE = -6
    URL_OPEN_TIMED_OUT = -7
    # Extensions
    FileExtensionAvailable = ['jpg', 'jpeg', 'gif', 'png', 'bmp']

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.videoStream = False
        self.imageStream = False
        if(self.verbose):
            print("Camera::__init__ with verbose=" + str(self.verbose))
        #self.video = cv2.VideoCapture(self.source)
    
    def __del__(self):
        if(self.videoStream == True):
            self.video.release()
    
    def bindVideoStream(self, source):
        self.videoStream = True
        self.imageStream = False
        self.source = source
        self.video = cv2.VideoCapture(self.source)
        if(self.verbose):
            print("Camera::bindVideoStream() to " + str(self.source))
    
    def releaseVideoStream(self):
        self.video.release()
        if(self.verbose):
            print("Camera::releaseVideoStream() released")
    
    def bindImageStream(self, url):
    	# download the image, convert it to a NumPy array, and then read
        # it into OpenCV format
        self.videoStream = False
        self.imageStream = True
        self.url = url
        if(self.verbose):
            print("Camera::bindImageStream() to " + self.url)

    def getFrame(self, extension):
        if(extension in Camera.FileExtensionAvailable == False):
            return Camera.FILE_EXTENSION_NOT_AVAILABLE, None
        
        if(self.videoStream == True):
            status, image = self.video.read()
            if(status == True):                    
                status, image = cv2.imencode("." + extension, image)
                if(self.verbose):
                    print("Camera::getFrame() from videoStream encoded to " + extension)
                return Camera.STATUS_OK, image
            else:
                if(self.verbose):
                    print("Camera::getFrame() from videoStream fails to encode image")
                return Camera.SOURCE_NOT_FOUND, None
        elif(self.imageStream == True):                        
            try:
                resp = urllib.urlopen(self.url, timeout=1)
            except urllib.URLError:
                if(self.verbose):
                    print("Camera::getFrame() from imageStream fails to open url, timedout")
                return Camera.URL_OPEN_TIMED_OUT, None
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)   
            status, image = cv2.imencode("." + extension, image)
            if(self.verbose):
                print("Camera::getFrame() from videoStream encoded to " + extension)
            return Camera.STATUS_OK, image
        else:
            return Camera.NO_STREAM_BINDED, None

    def getVersionOpenCV(self):
        return cv2.__version__

    def showImage(self, image):
        cv2.imshow("testes", image)  
        cv2.waitKey(0);
        cv2.destroyAllWindows()
    
    def saveImage(self, image, filename):
        # TODO verifica path imagem para n acessar diretorios que nao pode
        status = cv2.imwrite(filename, image)
        if(status == True):
            if(self.verbose):
                print("Camera::saveImage() done, filename=" + filename)
            return Camera.STATUS_OK
        else:
            if(self.verbose):
                print("Camera::saveImage() fails")
            return Camera.FAIL_TO_SAVE
                