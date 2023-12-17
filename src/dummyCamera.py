from camera import Camera
import time
class DummyCamera(Camera):
    imgs = [open('src/dummy/' + f + '.jpg', 'rb').read() for f in [str(i) for i in range(1, 39)]]

    @staticmethod
    def frames():
        while True:
            yield DummyCamera.imgs[int(time.time()) % 3]
            time.sleep(1)
