import cv2
from threading import Thread
from picamera2 import Picamera2


class Stream:
    def __init__(self):
        # initialize PiCamera2
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_preview_configuration(
            main={"format": "XRGB8888", "size": (640, 480)}))
        self.picam2.start()

        # grab first frame
        self.frame = self.picam2.capture_array()
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            self.frame = self.picam2.capture_array()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True
        self.picam2.stop()
