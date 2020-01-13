from flask import Flask, render_template, Response, send_file
from TCamera import Camera

app = Flask(__name__)

camera = Camera(verbose=True)

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/live_image')
def live_image():
    camera.bindImageStream("http://192.168.1.22:8081/?action=snapshot")
    rslt, img = camera.getFrame(".jpg")
    if(rslt == camera.STATUS_OK):
        return Response(b'--frame\r\n' + b'Content-Type: image/jpg\r\n\r\n' + img.tobytes() + b'\r\n\r\n', 
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return send_file('static/no-image.png', mimetype='image/png')


# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(VideoCamera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)