import io
import picamera
import time
from camera import Camera

class PiCamera(Camera):
    @staticmethod

    with picamera.PiCamera() as camera:
        # let camera warm up
        time.sleep(2)

        stream = io.BytesIO()
        for _ in camera.capture_continuous(stream, 'jpeg',
                                           use_video_port=True):
            # return current frame
            stream.seek(0)
            yield stream.read()

            # reset stream for next frame
            stream.seek(0)
            stream.truncate()