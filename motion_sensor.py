import sys
import time
import RPi.GPIO as GPIO
from time import sleep

import datetime
import time

SENSOR_PORT=5
LED_PORT=25
DELAY=1e-3

def led_init():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(SENSOR_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LED_PORT, GPIO.OUT)

def led_deinit():
  GPIO.cleanup()

class motion_sensor:
    def __init__(self, delay_from_last_motion=None, 
            on_callback=None, off_callback=None):
        self.last_motion_date \
            = datetime.datetime.now()
        self.delay_from_last_motion \
            = delay_from_last_motion
        self.on_callback = on_callback
        self.off_callback = off_callback
        self.on = False
        self.start()

    def start(self):
        try:
          led_init()
          print("start motion sensor")
        except:
          print("exception occurred")
          return 1
        else:
          while True:
            if GPIO.input(SENSOR_PORT):
              GPIO.output(LED_PORT, GPIO.HIGH)
              self.last_motion_date \
                  = datetime.datetime.now()
              if self.on_callback and not self.on:
                self.on_callback()
                self.on = True
            else:
              GPIO.output(LED_PORT, GPIO.LOW)
              if self.delay_from_last_motion and \
                      self.off_callback:
                if datetime.datetime.now() - \
                        self.last_motion_date > \
                        self.delay_from_last_motion:
                    if self.on:
                        self.off_callback()
                        self.on = False
            sleep(DELAY)
            print(self.on)
        finally:
          print("Finaly")
          led_deinit()

if __name__ == '__main__':
  ms = motion_sensor()
  ms.start()
