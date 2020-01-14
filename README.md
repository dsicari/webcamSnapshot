# webcamSnapshot
Get snapshot from a webcam with python using opencv and flask

video sample for tests
curl -L https://www.sample-videos.com/video123/mp4/720/big_buck_bunny_720p_10mb.mp4 -o big_buck_bunny_720p_10mb.mp4


<img id="bg" src="{{ url_for('live_image') }}">

para receber Response(b'--frame\r\n' b'Content-Type: image/jpg\r\n\r\n' + img.tobytes() + b'\r\n\r\n', 
                        mimetype='multipart/x-mixed-replace; boundary=frame')
