from flask import Flask, render_template, Response
import os

from dummyCamera import DummyCamera


app = Flask(__name__ , template_folder=os.path.abspath('src/templates'))


@app.route('/')
def index_html():  # put application's code here
    return render_template('index.html')



def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(DummyCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':
    app.run()
