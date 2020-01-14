from flask import Flask, render_template, Response, send_file
from TCamera import Camera
import base64

app = Flask(__name__)

camera = Camera(verbose=True)

@app.route('/status')
def status():
    return render_template('status.html')

# Para chamar rota url_for('view', variable='parameter', variable2='parameter2')
@app.route('/live_image/<format>')
def live_image(format):
    camera.bindImageStream("http://192.168.1.22:8081/?action=snapshot")
    #camera.bindVideoStream(0)
    rslt, img = camera.getFrame(".jpg")
    if(rslt == camera.STATUS_OK):
        if(format=="" or format=="raw"):
            return Response(b'--frame\r\n' + b'Content-Type: image/jpg\r\n\r\n' + img.tobytes() + b'\r\n\r\n', 
                            mimetype='multipart/x-mixed-replace; boundary=frame')
        elif(format=="base64"):
            base64Img = base64.b64encode(img)     
            return Response(b'--frame\r\n' + b'Content-Transfer-Encoding: base64\r\n\r\n' + b'Content-Type: image/jpg\r\n\r\n' + base64Img + b'\r\n\r\n', 
                            mimetype='multipart/x-mixed-replace; boundary=frame')
    return send_file('static/no-image.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)