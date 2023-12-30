import io
import picamera2
import time
from camera import Camera

# using PiCamera2


class PiCamera(Camera):
    @staticmethod
    def frames():
        with picamera2.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)

            with picamera2.array.PiRGBArray(camera) as stream:
                for _ in camera.capture_continuous(stream, "rgb", use_video_port=True):
                    # convert rgb to jpeg
                    jpegData = bytearray()
                    stream.rgb_array.tofile(jpegData, format="jpeg")

                    yield bytes(jpegData)

                    # reset stream for next frame
                    stream.truncate()
